from pathlib import Path
import os
import sys


#Carpeta base del proyecto (desarrollo)
#BASE_DIR = Path(__file__).resolve().parent
#Carpeta base del proyecto (compilado)
BASE_DIR = getattr(sys, '_MEIPASS', os.path.abspath('.'))

#Carpeta de assets
ASSETS_DIR = os.path.join(BASE_DIR, 'assets/')

#Carpeta de autenticación (credenciales, token, etc.)
AUTH_DIR = os.path.join(BASE_DIR, 'api/')

#Rutas de instalación local de minecraft
MINECRAFT_MODS_PATH = os.path.join(os.getenv('APPDATA'), '.minecraft/mods')
MINECRAFT_SHADERS_PATH = os.path.join(os.getenv('APPDATA'), '.minecraft/shaderpacks')
UNNECESSARY_FOLDER_NAME = 'amujeraos_unnecessary'
UNNECESSARY_MODS_PATH = os.path.join(MINECRAFT_MODS_PATH, UNNECESSARY_FOLDER_NAME)

#Drive
MODS_FOLDER_ID = '1AqsEcctxUZKkonbm-qf_eYoD3CgnE1W0'
FORGE_FOLDER_ID = '16MR3nq68HiKVnCDOkv-Ee0DvcE_go78_'
SHADERS_FOLDER_ID = '1skpsR8HndesUUMom6mR4Asqrt7_vBRFf'
SERVER_PROPS_ID = '1gr6WmDxg9r6TBz31-FLdL5b40OF1fe2a'

#Propiedades de autenticación
APP_CREDENTIALS = os.path.join(AUTH_DIR, 'credentials.json')
APP_TOKEN = os.path.join(AUTH_DIR, 'token.json')


#Propiedades de Interfaz
APP_VERSION = '1.3.0'
APP_NAME = 'Xuchetucraft'
APP_LAYER = 'Modpack Installer'
APP_DESCRIPTION = '''
Bienvenido a la beta de mi gestor de mods para Amujeraos Server. Aquí podrás:

1. Instalar la versión de Forge necesaria (próximamente)
2. Descargar todos los mods necesarios para acceder al servidor (shaders incluidos)

'''

#RELATIVE_ROUTES
APP_ICON = os.path.join(ASSETS_DIR, 'panda.ico')
APP_MAIN_IMAGE = os.path.join(ASSETS_DIR, 'novaskin-wallpaper-llama_cut.jpg')
APP_LOGO = os.path.join(ASSETS_DIR, 'xuchetucraft_logo.jpg')


APP_WIDTH = None
APP_HEIGHT = None
APP_X_POSITION = None
APP_Y_POSITION = None

#Sistema
SYSTEM_SCREEN_WIDTH = None
SYSTEM_SCREEN_HEIGHT = None

#Texto de interfaz
MAIN_TITLE = 'Titulo Principal'

#Colores
BACKGROUND_COLOR = '#2a2a2a' #Fondo (negro)
BACKGROUND_COLOR2 = '#c1d8e8' #Fondo (negro)
TEXT_COLOR = '#ffffff' #Texto (blanco)

#Botones (texto)
BTN_TEXT_NEXT = 'Continuar'
BTN_TEXT_CANCEL = 'Cancelar'
BTN_TEXT_BACK = 'Volver'
BTN_TEXT_RELOAD = 'Recargar'
BTN_TEXT_DELETE = 'Eliminar'
BTN_TEXT_FINISH = 'Finalizar'
BTN_TEXT_MENU_OPTION_1 = 'Instalar Forge'
BTN_TEXT_MENU_OPTION_2 = 'Instalar mods'

#Frames (textos)
OPTION_2_TITLE = "Instalar mods"
OPTION_2_CHECKBOX_1 = 'Mover mods sobrantes a subdirectorio dentro de "mods"'
OPTION_2_CHECKBOX_2 = "Eliminar mods sobrantes"