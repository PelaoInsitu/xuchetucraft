from interface import tkinter_root as tkroot
from utils import clean_incomplete_files
from settings import MINECRAFT_MODS_PATH

#Borrar mods dañados o incompletos
clean_incomplete_files(MINECRAFT_MODS_PATH)

#Arranque de ventana root
root = tkroot.start()

root.mainloop()