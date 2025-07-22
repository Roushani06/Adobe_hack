from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextBoxHorizontal
import re
import os

class PDFProcessor:
    def _init_(self, file_path):
        self.file_path = file_path
        self.title = ""
        self.outline = []
        self.font_thresholds = {'h1': 20, 'h2': 16, 'h3': 14}
        self.hindi_fixes = {
            r'पंचतं\s?क': 'पंचतंत्र की',
            r'आचाय\s?वणु': 'आचार्य विष्णु',
            r'शमा': 'शर्मा',
            r'कहानयां': 'कहानियां',
            r'(\S)ं': r'\1ं',
            r'(\S)़': r'\1़',
            r'(\S)ि': r'\1ि',
            r'(\S)ु': r'\1ु'
        }

    def extract_outline(self):
        try:
            self._detect_font_thresholds()
            for page_num, page_layout in enumerate(extract_pages(self.file_path)):
                for element in page_layout:
                    if isinstance(element, LTTextBoxHorizontal):
                        for text_line in element:
                            if isinstance(text_line, LTTextContainer):
                                self._process_text_element(text_line, page_num)
            
            if not self.title and self.outline:
                self.title = self.outline[0]['text']
            
            return {
                "title": self.title or os.path.basename(self.file_path),
                "outline": self.outline
            }
        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            return {
                "title": os.path.basename(self.file_path),
                "outline": []
            }

    def _clean_text(self, text):
        text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
        for pattern, replacement in self.hindi_fixes.items():
            text = re.sub(pattern, replacement, text)
        text = ' '.join(text.split()).strip().rstrip('.:,-')
        return text

    def _detect_font_thresholds(self):
        font_sizes = []
        for page_layout in extract_pages(self.file_path):
            for element in page_layout:
                if isinstance(element, LTTextBoxHorizontal):
                    for text_line in element:
                        if isinstance(text_line, LTTextContainer):
                            font_size = self._get_font_size(text_line)
                            if font_size > 10:
                                font_sizes.append(font_size)
        
        if font_sizes:
            font_sizes = sorted(font_sizes)
            n = len(font_sizes)
            self.font_thresholds = {
                'h1': font_sizes[int(0.9 * n)] if n > 10 else 20,
                'h2': font_sizes[int(0.7 * n)] if n > 10 else 16,
                'h3': font_sizes[int(0.5 * n)] if n > 10 else 14
            }

    def _process_text_element(self, text_line, page_num):
        raw_text = text_line.get_text()
        text = self._clean_text(raw_text)
        if not text:
            return
        
        font_size = self._get_font_size(text_line)
        level = None
        if font_size >= self.font_thresholds['h1']:
            level = "H1"
        elif font_size >= self.font_thresholds['h2']:
            level = "H2"
        elif font_size >= self.font_thresholds['h3']:
            level = "H3"
        
        if level and self._is_heading(text):
            if level == "H1" and not self.title:
                self.title = text
            self.outline.append({
                "level": level,
                "text": text,
                "page": page_num
            })

    def _get_font_size(self, text_line):
        try:
            return text_line._objs[0].size
        except:
            return 0

    def _is_heading(self, text):
        text_clean = text.lower().strip()
        hi_patterns = r'^(अध्याय|भाग|परिचय|निष्कर्ष|सारांश|संदर्भ|कहानी|शिक्षा)'
        en_patterns = r'^(chapter|section|part|appendix|introduction|conclusion)'
        return (re.search(hi_patterns, text_clean) or 
                re.search(en_patterns, text_clean, re.IGNORECASE) or
                re.match(r'^(\d+\.)+\s', text) or
                len(text.split()) <= 10)