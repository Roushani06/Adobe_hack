import fitz, json, os

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = ""
    # --- Extract Title from first page ---
    if doc.page_count > 0:
        page0 = doc.load_page(0)
        spans = []
        for block in page0.get_text("dict")["blocks"]:
            if block["type"] != 0: 
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    spans.append((span["size"], span["text"].strip()))
        # Choose spans with largest sizes (e.g. >= 24 pt)
        big_spans = [text for (size, text) in spans if size >= 24]
        # Join unique pieces
        title = " ".join(dict.fromkeys(big_spans)).strip()
        # Fallback: if empty, use first block text
        if not title:
             lines = page0.get_text().splitlines()
             if lines:
              title = lines[0].strip()
             else:
              title = "Untitled Document"

    # --- Extract Headings from remaining pages ---
    for page_index in range(1, doc.page_count):
        page = doc.load_page(page_index)
        page_num = page_index + 1  # 1-based page numbering
        text_dict = page.get_text("dict")
        for block in text_dict["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                line_text = "".join(span["text"] for span in line["spans"]).strip()
                if not line_text:
                    continue
                # Determine max font size and style for this line
                max_size = max(span["size"] for span in line["spans"])
                fonts = {span["font"] for span in line["spans"]}
                is_bold = any("Bold" in f or "Black" in f for f in fonts)
                is_italic = any("Italic" in f for f in fonts)
                level = None
                # Heuristics for heading levels
                if page_index == 1 and max_size >= 15:
                    # On page 2: treat large text as H1 until we hit smaller headings
                    level = "H1"
                elif is_bold and max_size >= 12:
                    # Bold 12pt+ often H2 (e.g. "Summary", "Background", "Appendix ...")
                    level = "H2"
                elif line_text.endswith(":") and (is_bold or is_italic or max_size >= 11):
                    # Lines ending with ':' often H3 (subsections)
                    level = "H3"
                elif is_bold and max_size >= 11:
                    # Bold ~11pt (like "For each...") as H4
                    level = "H4"
                if level:
                    outline.append({"level": level, "text": line_text, "page": page_num})
    return {"title": title, "outline": outline}

def process_all_pdfs(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        if not fname.lower().endswith(".pdf"): 
            continue
        infile = os.path.join(input_dir, fname)
        result = extract_outline_from_pdf(infile)
        outname = os.path.splitext(fname)[0] + ".json"
        with open(os.path.join(output_dir, outname), "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

if __name__ == "__main__":
    process_all_pdfs("/app/input", "/app/output")
