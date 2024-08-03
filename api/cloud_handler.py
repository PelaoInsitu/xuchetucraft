import os
from googleapiclient.discovery import build
from .authentication import GoogleDriveAuth
from googleapiclient.http import MediaIoBaseDownload
import tkinter as tk
import io


class GoogleDriveHandler:

    #Buscar archivos en Drive
    @classmethod
    def search_files(cls, folder_id):
        creds = GoogleDriveAuth.authenticate2()
        service = build('drive', 'v3', credentials=creds)

        files = []
        page_token = None

        while True:
            results = service.files().list(
                q=f"'{folder_id}' in parents",
                fields="nextPageToken, files(name, id)",
                pageToken=page_token
            ).execute()

            items = results.get('files', [])
            files.extend(items)

            page_token = results.get('nextPageToken')
            if not page_token:
                break

        return files


    
    #Descargar archivos
    @classmethod
    def download_files(cls, files, path, progress_bar, root):
        creds = GoogleDriveAuth.authenticate2()
        service = build('drive', 'v3', credentials=creds)
        total_files = len(files)

        os.mkdir(path) if not os.path.exists(path) else None

        for index, file in enumerate(files, start=1):
            request = service.files().get_media(fileId=file['id'])
            ruta_destino_local = os.path.join(path, file['name'])

            if not os.path.exists(ruta_destino_local):
                try:
                    fh = io.FileIO(ruta_destino_local, 'wb')
                    downloader = MediaIoBaseDownload(fh, request)

                    done = False
                    while not done:
                        status, done = downloader.next_chunk()
                
                except Exception as e:
                    os.remove(ruta_destino_local) if os.path.exists(ruta_destino_local) else None
                    #print(f"Descargado {int(status.progress() * 100)}%.")

                #print(f'Archivo descargado en: {ruta_destino_local}')

            else:
                #print(f"archivo {file['name']} ya existe.")
                pass

            #Actualizar barra de progreso
            #if ( total_files > 0):
            progress_value = int((index / total_files) * 100)
            progress_bar['value'] = progress_value
            root.update_idletasks()

    
    @classmethod
    def download_server_props_json(cls, file_id):
        # Autenticar
        creds = GoogleDriveAuth.authenticate2()
        service = build('drive', 'v3', credentials=creds)

        # Descargar contenido del archivo
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
            #print(f"Descargado {int(status.progress() * 100)}%.")

        content = fh.getvalue()

        return content
    

    @classmethod
    def get_modloader_file(cls, folder_id):
        creds = GoogleDriveAuth.authenticate2()
        service = build('drive', 'v3', credentials=creds)

        # Busca archivos dentro de la carpeta
        query = f"'{folder_id}' in parents"
        results = service.files().list(
            q=query,
            fields="files(id, name)",
            pageSize=10  # Ajusta el tamaño si es necesario
        ).execute()

        files = results.get('files', [])
        if files:
            # Suponiendo que hay solo un archivo, devolvemos el primero
            return files[0]  # Devolver el primer archivo encontrado
        else:
            return None
        
    
    @classmethod
    def download_file(cls, folder_id, destination_path):
        # Obtener el archivo de la carpeta
        file_info = GoogleDriveHandler.get_modloader_file(folder_id)
        if file_info:
            file_id = file_info['id']
            file_name = file_info['name']
            full_path = os.path.join(destination_path, file_name)

            # Crear el directorio de destino si no existe
            os.makedirs(destination_path, exist_ok=True)

            if os.path.exists(full_path):
                return full_path

            # Autenticación y construcción del servicio
            creds = GoogleDriveAuth.authenticate2()  # Asegúrate de haber importado GoogleDriveAuth
            service = build('drive', 'v3', credentials=creds)

            # Solicitar el archivo
            request = service.files().get_media(fileId=file_id)

            # Descargar el archivo
            with open(full_path, 'wb') as file:
                downloader = MediaIoBaseDownload(file, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    #print(f"Descargado {int(status.progress() * 100)}%.")

            #print(f"Archivo descargado y guardado en {full_path}")

            return full_path
        else:
            print("No file found in the specified folder.")