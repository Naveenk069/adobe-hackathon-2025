# round1b_main.py
import json
import os
import time
import glob
from utils.section_splitter import extract_sections
from utils.relevance_scorer import score_sections, extract_subsections

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def main():
    start = time.time()

    # 🔍 Find first JSON input file (any name)
    json_files = glob.glob(os.path.join(INPUT_DIR, "*.json"))
    if not json_files:
        print("❌ No JSON input file found in ./input/")
        return

    persona_path = json_files[0]
    print(f"📥 Using input file: {os.path.basename(persona_path)}")

    # 📖 Load and parse JSON file
    with open(persona_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    # 🧠 Extract persona and job from either flat or nested structure
    if "persona" in meta and isinstance(meta["persona"], dict):
        persona = meta["persona"].get("role", "").strip()
        job = meta.get("job_to_be_done", {}).get("task", "").strip()
    elif "persona" in meta and isinstance(meta["persona"], str):
        persona = meta["persona"].strip()
        job = meta.get("job", "").strip()
    else:
        print("❌ Unsupported input JSON format.")
        return

    if not job:
        print("❌ Missing job/task description in JSON.")
        return

    # 📄 Get list of input PDFs
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("❌ No PDF files found in ./input/")
        return

    all_sections = []

    # 📚 Process each PDF
    for file in pdf_files:
        pdf_path = os.path.join(INPUT_DIR, file)
        print(f"🔍 Extracting from: {file}")
        sections = extract_sections(pdf_path)
        for section in sections:
            section["document"] = file
        all_sections.extend(sections)

    # 🎯 Relevance scoring and refinement
    scored = score_sections(all_sections, job)
    refined = extract_subsections(scored)

    # 📦 Format final output
    result = {
        "metadata": {
            "input_documents": pdf_files,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        },
        "extracted_sections": scored[:5],
        "subsection_analysis": refined
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "result.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("✅ Output written to:", output_path)
    print("⏱️ Completed in %.2f seconds" % (time.time() - start))


if __name__ == "__main__":
    main()
