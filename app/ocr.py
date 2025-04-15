import easyocr
import numpy as np
from PIL import Image
import io

reader = easyocr.Reader(['fa', 'en'])

def perform_ocr(image_bytes):
    try:
        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to numpy array
        image_np = np.array(image)
        
        # Perform OCR
        results = reader.readtext(image_np, detail=0, paragraph=True)
        
        # Join lines with newline characters
        extracted_text = '\n'.join(results)
        
        return extracted_text
    except Exception as e:
        return f"خطا در پردازش تصویر: {str(e)}"