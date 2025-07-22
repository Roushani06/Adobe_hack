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

