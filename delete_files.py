import os
import glob
import shutil


def delete_files_download(downloads_folder):

    pdf_files = glob.glob(os.path.join(downloads_folder, '*.pdf'))

    for pdf_file in pdf_files:
        try:
            os.remove(pdf_file)
            print(f"Arquivo apagado: {pdf_file}")
        except Exception as e:
            print(f"Erro ao apagar o arquivo {pdf_file}: {e}")

    return None


def delete_folders(target_folder):
    items = os.listdir(target_folder)

    for item in items:
        item_path = os.path.join(target_folder, item)
        if os.path.isdir(item_path):  
            try:
                shutil.rmtree(item_path) 
                print(f"Pasta apagada: {item_path}")
            except Exception as e:
                print(f"Erro ao apagar a pasta {item_path}: {e}")
