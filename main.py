from utils.ocr import extract_text_with_boxes
from utils.color_detect import detect_colored_boxes
from utils.rule_mapper import map_rules
import json

image_path = "sample.png"

# Step 1: OCR with positions
ocr_data = extract_text_with_boxes(image_path)

# Step 2: Detect colored boxes
box_data = detect_colored_boxes(image_path)

# Step 3: Match text to colored boxes with rule logic
final_data = map_rules(ocr_data, box_data)

# Step 4: Save as structured JSON
with open("output.json", "w") as f:
    json.dump(final_data, f, indent=4)

print("✅ Extraction complete. Saved as output.json")
