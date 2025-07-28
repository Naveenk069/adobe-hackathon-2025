# utils/relevance_scorer.py
import nltk
from nltk.tokenize import sent_tokenize

def score_sections(sections, job_desc):
    keywords = set(job_desc.lower().split())
    scored = []
    for section in sections:
        text = section["section_title"].lower()
        match_count = sum(1 for word in keywords if word in text)
        score = match_count / len(keywords)
        if score > 0:  # discard unrelated
            section["importance_rank"] = round(score, 3)
            scored.append(section)
    return sorted(scored, key=lambda x: -x["importance_rank"])

def extract_subsections(sections, top_n=5):
    refined = []
    for sec in sections[:top_n]:
        text = sec["section_title"]
        summary = sent_tokenize(text)[0]
        refined.append({
            "document": sec["document"],
            "page": sec["page"],
            "refined_text": summary,
            "importance_rank": sec["importance_rank"]
        })
    return refined
