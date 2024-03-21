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

        results = service.files().list(
            q=f"'{folder_id}' in parents",
            fields="files(name, id)"
        ).execute()

        files = results.get('files', [])

        if files:
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