from utils import (
    extract_images_from_pdf,
    easyocr_images,
    tesseract_ocr_images,
    generate_doc
)
import torch

pdf_path = 'simulacionross.pdf'
docx_path = 'output.doc'
lang = 'es'
device = 'cuda' if torch.cuda.is_available() else 'cpu'


images = extract_images_from_pdf(pdf_path)
print('#'*20)
print('PASO UNO SUPERADO')
print('#'*20)


# text = easyocr_images(images, lang, device)
lang='spa'
text = tesseract_ocr_images(images, lang)

print('#'*20)
print('PASO DOS SUPERADO')
print('#'*20)

generate_doc(text)
print(f"Texto guardado en {docx_path}")

print('#'*20)
print('PASO TRES SUPERADO')
print('#'*20)


print(text)