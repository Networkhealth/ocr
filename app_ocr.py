# OCR functionality implementation
import pytesseract
from PIL import Image

def perform_ocr(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image, lang='fas')  # 'fas' for Persian