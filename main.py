import os
from utils import FOLDER_PATH, FILES_PATH
from api_keys import GEMINI_API_KEY
from pdf_extract import extract_text_from_pdf
from generative_ai import generative_ai_text
from convert_pdf_to_image import convert_to_image
from twitter import make_twitter_post
from delete_files import delete_files_download, delete_folders

if __name__ == "__main__":

    for pdf_name in os.listdir(FOLDER_PATH):
        if pdf_name.endswith('.pdf'):

            #1
            pdf_path = FOLDER_PATH + pdf_name
            text = extract_text_from_pdf(pdf_path)
            print("TEXTO EXTRAIDO DO PDF")

            #2
            response = generative_ai_text(GEMINI_API_KEY, "gemini-pro", text)
            print(f"TEXTO CRIADO PELA IA COM TAMANHO DE {len(response.text)} caracteres")
            print(response.text)
            texto = response.text
            if len(texto) > 280:
                # Corta o texto no caractere 279
                texto = texto[:279]
            

            #3
            convert_to_image(FOLDER_PATH, FILES_PATH, pdf_name)
            print("PDF CONVERTIDO EM IMAGEM")

            #4
            make_twitter_post(FILES_PATH, pdf_name, texto)
            print("TWEET POSTADO")

            #5
    delete_files_download(FOLDER_PATH)

    delete_folders(FILES_PATH)


