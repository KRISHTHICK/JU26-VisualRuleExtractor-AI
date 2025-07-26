def map_rules(text_boxes, color_boxes):
    results = []
    for cb in color_boxes:
        x1, y1, w, h = cb["box"]
        x2, y2 = x1 + w, y1 + h
        matched_text = []

        for tb in text_boxes:
            tx, ty = tb["left"], tb["top"]
            if x1 <= tx <= x2 and y1 <= ty <= y2:
                matched_text.append(tb["text"])

        results.append({
            "BoxColor": cb["color"],
            "Position": cb["box"],
            "TextInside": " ".join(matched_text),
            "Type": infer_box_type(matched_text)
        })
    return results

def infer_box_type(texts):
    joined = "".join(texts)
    if '.' in joined:
        return "Decimal Input Box"
    elif joined.isalpha():
        return "Alphanumeric Box"
    return "Empty or Symbol Box"
