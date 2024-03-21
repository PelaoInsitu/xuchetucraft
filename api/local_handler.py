import os
from api.cloud_handler import GoogleDriveHandler
from settings import MODS_FOLDER_ID, MINECRAFT_MODS_PATH, UNNECESSARY_FOLDER_NAME, UNNECESSARY_MODS_PATH
import tkinter as tk
import shutil


class LocalHandler():
    #Ruta de instalación local de Minecraft para mods
    #MINECRAFT_MODS_PATH = os.path.join(os.getenv('APPDATA'), '.minecraft/mods')

    #Ruta para mover mods no requeridos en el servidor
    #UNNECESSARY_FOLDER_NAME = 'amujeraos_unnecessary'
    #UNNECESSARY_MODS_PATH = os.path.join(MINECRAFT_MODS_PATH, UNNECESSARY_FOLDER_NAME)

    #Obtener lista de archivos de google drive (mods requeridos)
    REQUIRED_FILES = GoogleDriveHandler.search_files(MODS_FOLDER_ID)


    @classmethod
    def get_missing_files(cls):
        missing_files = []
        required_files = cls.REQUIRED_FILES

        for file in required_files:
            file_path = os.path.join(MINECRAFT_MODS_PATH, file['name'])

            if not os.path.exists(file_path):
                missing_files.append({'name':file['name'], 'id':file['id']})
        
        return missing_files
    

    @classmethod
    def get_excess_files(cls):
        excess_files = []
        raw_required_files = cls.REQUIRED_FILES
        required_files = []

        if not os.path.exists(MINECRAFT_MODS_PATH):
            os.mkdir(MINECRAFT_MODS_PATH)
            
        #Obtener lista de archivos existentes en el cliente y excluir las carpetas
        raw_local_files = os.listdir(MINECRAFT_MODS_PATH)
        exist_files = [file for file in raw_local_files if not os.path.isdir(os.path.join(MINECRAFT_MODS_PATH, file))]

        for file in raw_required_files:
            required_files.append(file['name'])


        for file in exist_files:
            if not file in required_files:
                excess_files.append(file)
        
        return excess_files
    

    @classmethod
    def insert_tkinter_list(cls, tkinter_list, files):
        if len(files) == 0:
            tkinter_list.insert(tk.END, "No se encontraron mods")
        
        else:
            for file in files:
                if isinstance(file, dict) and "name" in file:
                    tkinter_list.insert(tk.END, file["name"])
                    #print(file["name"])

    
    @classmethod
    def insert_tkinter_list_2(cls, tkinter_list, files):
        if len(files) == 0:
            tkinter_list.insert(tk.END, "No se encontraron mods")
        
        else:
            for file in files:
                tkinter_list.insert(tk.END, file)
                #print(file)


    @classmethod
    def move_files(cls, list):
        if len(list) > 0:
            if not os.path.exists(UNNECESSARY_MODS_PATH):
                cls.create_folder(UNNECESSARY_MODS_PATH)
                
            for file in list:
                file_path = os.path.join(MINECRAFT_MODS_PATH, file)
                destination_file_path = os.path.join(UNNECESSARY_MODS_PATH, file)

                if os.path.exists(file_path):
                    shutil.move(file_path, destination_file_path)
                    #print(f"Archivo '{file}' movido a {UNNECESSARY_MODS_PATH}")

                else:
                    #print(f"El archivo '{file}' no existe en la ubicación original.")
                    pass


    @classmethod
    def delete_files(cls, list):
        if len(list) > 0:
            for file in list:
                file_path = os.path.join(MINECRAFT_MODS_PATH, file)

                if os.path.exists(file_path):
                    os.remove(file_path)
                    #print(f"Archivo '{file}' eliminado")
                else:
                    #print(f"El archivo '{file}' no existe en la ubicación original.")
                    pass


    @classmethod
    def create_folder(cls, path):
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            #print(f'Error al crear la carpeta: {e}')
            pass