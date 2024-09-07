import io
import easyocr
import fitz
import numpy as np
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from docx import Document


def extract_images_from_pdf(pdf_path):
    images = []
    images = convert_from_path(pdf_path)
    return images


def easyocr_images(images, lang, device):
    reader = easyocr.Reader([f'{lang}'], gpu=(device=='cuda'))
    text = ''
    for image in images:
        image_np = np.array(image)
        result = reader.readtext(image_np)
        for res in result:
            text += res[1] + '\n'
    return text

def tesseract_ocr_images(images, language):
    text = ''
    for image in images:
        image_np = np.array(image)
        text += pytesseract.image_to_string(image_np, lang=language) + '\n'
    return text

def generate_doc(text, docx_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(docx_path)
