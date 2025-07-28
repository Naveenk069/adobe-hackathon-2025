import os
import json
from utils.heading_extractor import HeadingExtractor

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Process each PDF in input
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            print(f"📄 Processing: {filename}")

            try:
                extractor = HeadingExtractor(input_path)
                result = extractor.extract()

                output_filename = filename.replace(".pdf", ".json")
                output_path = os.path.join(OUTPUT_DIR, output_filename)

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                print(f"✅ Saved: {output_filename}")
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
