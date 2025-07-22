import os
import json
from src.pdf_processor import PDFProcessor

def process_pdfs():
    is_docker = os.environ.get('RUNNING_IN_DOCKER', '').lower() == 'true'
    input_dir = "/app/input" if is_docker else "./input"
    output_dir = "/app/output" if is_docker else "./output"
    
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Processing PDFs from: {input_dir}")
    
    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.json"
            output_path = os.path.join(output_dir, output_filename)
            
            print(f"Processing: {filename} → {output_filename}")
            
            processor = PDFProcessor(input_path)
            result = processor.extract_outline()
            
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

if _name_ == "_main_":
    process_pdfs()