# JU26-VisualRuleExtractor-AI
GEN AI

"VisualRuleExtractor-AI: Extract Semantic and Visual Layout Rules from Structured Process Documents using Python"
🧠 Step-by-Step Overview
Step	Task
1	Use OCR + Layout Analysis to extract text, tables, boxes
2	Detect bounding boxes, their fill color, and text (e.g., decimal values)
3	Store patterns/rules (like yellow box = quantity input) in a config/rules file
4	Output structured JSON (or XML) maintaining order and semantic mapping

📦 Python Tools Used
Task	Library
OCR	pytesseract, easyocr
Box & Color Detection	opencv, PIL, numpy
Layout Parsing	layoutparser, pdf2image
Rules Mapping	JSON-based config files
Final Output	Structured JSON / XML

🧪 Sample Output (Example JSON)
json
Copy
Edit
{
  "Section": "Part A",
  "Title": "Process All Warehouse Issued Materials",
  "Steps": [
    {
      "Step": "01",
      "Description": "Record the details of Bactrinish Unsolved (QAS152) for SAP",
      "Fields": [
        {
          "Label": "Quantity (Line 1)",
          "BoxColor": "Yellow",
          "Value": "• .",
          "Type": "Decimal Input Box"
        },
        {
          "Label": "Batch Number (Line 1)",
          "BoxColor": "Yellow",
          "Value": "□□□□□□□",
          "Type": "Alphanumeric Box"
        }
      ]
    }
  ]
}

