
---

## 🧾 Round 1B: README.md

```markdown
# 🧠 Adobe Hackathon Round 1B – Persona-Driven Document Intelligence

## 🚀 Overview

This project builds an intelligent system that extracts and ranks the most relevant sections from a collection of PDF documents based on a **persona** and a **job-to-be-done**.

The goal is to act as a virtual analyst who scans documents and highlights only what matters to the user.

---

## ✅ Features

- 🧑‍💼 Persona + Task-aware PDF analysis
- 📄 Extracts and ranks most important sections and sub-sections
- 🔍 Highlights relevance for specific roles (e.g., HR, Researchers, Analysts)
- 🧠 Modular NLP pipeline (no GPU, no internet)
- 📦 Outputs structured JSON ready for downstream UX

---

## 🗃️ Input Format

All files go in `/input/`:
- Any number of `.pdf` documents (min: 3)
- One `.json` config file with persona + task + document metadata  
  (any name is allowed)

### 📝 Example JSON (input):
```json
{
  "persona": {
    "role": "HR professional"
  },
  "job_to_be_done": {
    "task": "Create and manage fillable forms for onboarding and compliance."
  },
  "documents": [
    {
      "filename": "Learn Acrobat - Fill and Sign.pdf",
      "title": "Learn Acrobat - Fill and Sign"
    },
    ...
  ]
}

## Output Format

{
  "metadata": {
    "input_documents": [...],
    "persona": "HR professional",
    "job_to_be_done": "Create and manage fillable forms for onboarding and compliance.",
    "processing_timestamp": "2025-07-28T12:00:00Z"
  },
  "extracted_sections": [
    {
      "document": "filename.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 4
    },
    ...
  ],
  "subsection_analysis": [
    {
      "document": "filename.pdf",
      "refined_text": "This section covers key insights...",
      "page_number": 4
    },
    ...
  ]
}

How to Build and Run

# Build Docker image
docker build --platform linux/amd64 -t pdf-round1b:local .

# Run container (adjust paths for Windows)
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-round1b:local

Repo Structure

/input             → PDFs + persona JSON  
/output            → result.json  
round1b_main.py    → main execution script  
utils/             → modular code: section_splitter, scorer  
Dockerfile         → build file  
README.md          → this file  
