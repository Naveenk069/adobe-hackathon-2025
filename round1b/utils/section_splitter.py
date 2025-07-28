# utils/section_splitter.py
import fitz

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    font_map = {}
    section_list = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                text = " ".join([span["text"] for span in line["spans"]]).strip()
                if not text or len(text) < 4:
                    continue
                size = round(line["spans"][0]["size"], 2)
                font_map[size] = font_map.get(size, 0) + 1
                section_list.append((size, text, page_num + 1))

    ranked_fonts = sorted(font_map.keys(), reverse=True)
    font_levels = {}
    if ranked_fonts: font_levels[ranked_fonts[0]] = "H1"
    if len(ranked_fonts) > 1: font_levels[ranked_fonts[1]] = "H2"
    if len(ranked_fonts) > 2: font_levels[ranked_fonts[2]] = "H3"

    structured = []
    for size, text, page in section_list:
        if size in font_levels:
            structured.append({
                "document": pdf_path.split("/")[-1],
                "page": page,
                "section_title": text,
                "level": font_levels[size]
            })
    return structured
