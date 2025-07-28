# 🔍 Adobe Hackathon Round 1A – Structured Outline Extractor

## 🚀 Overview

This project implements a fast, offline solution that takes in a PDF (up to 50 pages) and outputs a clean, hierarchical outline with Title and Headings (H1, H2, H3) for each page.

The goal is to help machines understand and summarize PDF structure to power semantic search, insight generation, and future document experiences.

---

## ✅ Features

- 📄 PDF-to-Outline Converter
- 🧠 Heuristic + Semantic Heading Classification
- ⚡ Runs completely offline in Docker (no network)
- ⏱️ Executes within 10 seconds for a 50-page PDF
- 🧬 Multilingual text support (if implemented)
- 🐍 Lightweight: Python-only, model-free or ≤ 200MB model

---

## 🗃️ Input Format

Place one or more PDFs in the `/input/` directory.

Example:
input/
└── sample.pdf


---

## 📤 Output Format

Each PDF gets a corresponding `.json` output in `/output/` with the following structure:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}


How to Build and Run :

# Step 1: Build Docker image
docker build --platform linux/amd64 -t pdf-extractor:local .

# Step 2: Run the container
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-extractor:local


Repo Structure

/input           → input PDFs  
/output          → output .json files  
Dockerfile       → build definition  
main.py          → PDF outline extractor
README.md        → this file


---