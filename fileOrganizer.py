import os
import shutil

directory = input("Introduzca el directorio a ordenar: ")
files = os.listdir(directory)  # Lista de archivos en el directorio
file_extensions = {
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"],
    "Video": [".mp4", ".mkv", ".MKV", ".flv", ".mpeg"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".doc", ".pdf", ".txt", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Comprimidos": [".zip", ".rar"],
    "Programas": [".exe", ".msi", ".deb", ".pkg", ".dmg", ".apk", ".bat"]
}

def fileOrganizer():
    for file in files:
        for category, extensions in file_extensions.items():
            for extension in extensions:
                if file.endswith(extension):
                    directory_path = os.path.join(directory, category)
                    if not os.path.exists(directory_path):
                        os.mkdir(directory_path)
                    shutil.move(os.path.join(directory, file), os.path.join(directory_path, file))

command = input("¿Quieres organizar los archivos? (S/N): ")
if command.upper() == "S":
    fileOrganizer()
    print("¡Archivos organizados con éxito!")
else:
    print("¡Archivos no organizados!")
