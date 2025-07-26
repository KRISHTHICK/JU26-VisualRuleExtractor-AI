import pytesseract
from PIL import Image
import cv2

def extract_text_with_boxes(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
    results = []
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 40:
            results.append({
                "text": data['text'][i],
                "conf": int(data['conf'][i]),
                "left": data['left'][i],
                "top": data['top'][i],
                "width": data['width'][i],
                "height": data['height'][i]
            })
    return results
