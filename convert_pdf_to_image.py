import os
from pdf2image import convert_from_path


def convert_to_image(FOLDER_PATH, FILES_PATH, pdf_name):
    pdf_name = pdf_name
    pdf_path = FOLDER_PATH + pdf_name

    image_path = FILES_PATH + pdf_name

    os.makedirs(image_path)

    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):
        final_image_path = f'{image_path}/{pdf_name}_page_{i+1}.jpg'
        page.save(final_image_path, 'JPEG')


