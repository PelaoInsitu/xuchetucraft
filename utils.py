import sys
import os
from interface.window import WindowApp
import tkinter as tk

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

## Ejemplo de uso
#ruta_al_archivo = resource_path("archivo.json")
#with open(ruta_al_archivo, "r") as archivo:
#    contenido = archivo.read()
#    # Trabaja con el contenido del archivo



def copy_to_clipboard(pattern, text):
    pattern.clipboard_clear()
    pattern.clipboard_append(text)
    pattern.update()
    #print("texto copiado al portapapeles")


def get_width_root():
    temp_root = tk.Tk()
    screen_width = temp_root.winfo_screenwidth()
    width = int(WindowApp.set_width(screen_width)*0.8)
    temp_root.destroy()
    return int(width)


def clean_incomplete_files(directory):
    os.mkdir(directory) if not os.path.exists(directory) else None
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
            os.remove(filepath)