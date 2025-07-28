# utils/heading_extractor.py

import fitz

class HeadingExtractor:
    def __init__(self, pdf_path):
        self.doc = fitz.open(pdf_path)
        self.title = ""
        self.outline = []

    def extract(self):
        font_sizes = {}
        headings = []

        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" not in block:
                    continue
                for line in block["lines"]:
                    text = " ".join([span["text"] for span in line["spans"]]).strip()
                    if not text or len(text) < 3:
                        continue

                    font_size = round(line["spans"][0]["size"], 2)
                    font_sizes[font_size] = font_sizes.get(font_size, 0) + 1
                    headings.append((font_size, text, page_num + 1))

        # Step 1: Determine font size rankings
        ranked_fonts = sorted(font_sizes.items(), key=lambda x: -x[0])
        font_size_to_level = {}
        if ranked_fonts:
            font_size_to_level[ranked_fonts[0][0]] = "H1"
        if len(ranked_fonts) > 1:
            font_size_to_level[ranked_fonts[1][0]] = "H2"
        if len(ranked_fonts) > 2:
            font_size_to_level[ranked_fonts[2][0]] = "H3"

        for font_size, text, page_num in headings:
            level = font_size_to_level.get(font_size)
            if level:
                self.outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num
                })

        # Title: first H1 text or largest font on first page
        for item in self.outline:
            if item["level"] == "H1" and item["page"] == 1:
                self.title = item["text"]
                break
        if not self.title and self.outline:
            self.title = self.outline[0]["text"]

        return {
            "title": self.title,
            "outline": self.outline
        }
