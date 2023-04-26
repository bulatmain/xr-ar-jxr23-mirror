from easyocr import Reader


READER = Reader(['ru'], gpu=False)

def get_text_from_image(image):
    texts = READER.readtext(image, detail=0)
    texts.append('')
    return texts
