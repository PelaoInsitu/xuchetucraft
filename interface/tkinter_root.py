import tkinter as tk
from interface.window import WindowApp as App
from interface.frames import main_frame
import settings as st

def start():
    #Instancia tkinter
    root = tk.Tk()

    #Resolución de pantalla
    st.SYSTEM_SCREEN_WIDTH = root.winfo_screenwidth()
    st.SYSTEM_SCREEN_HEIGHT = root.winfo_screenheight()


    #PROPIEDADES DE VENTANA
    #Dimensiones
    st.APP_WIDTH = App.set_width(st.SYSTEM_SCREEN_WIDTH) #Ancho
    st.APP_HEIGHT = App.set_height(st.SYSTEM_SCREEN_HEIGHT) #Alto
    st.APP_X_POSITION = App.set_x_position(st.SYSTEM_SCREEN_WIDTH, st.APP_WIDTH) #Posición eje x
    st.APP_Y_POSITION = App.set_y_position(st.SYSTEM_SCREEN_HEIGHT, st.APP_HEIGHT) #Posición eje y
    #Establecer propiedades
    root.title(f"{st.APP_NAME} - {st.APP_LAYER} ({st.APP_VERSION})") #Título
    root.geometry(f'{st.APP_WIDTH}x{st.APP_HEIGHT}+{st.APP_X_POSITION}+{st.APP_Y_POSITION}') #Establecer dimensiones y posición
    root.resizable(False, False) #Denegar redimensión
    root.iconbitmap(st.APP_ICON) #Icono
    root.configure(bg=st.BACKGROUND_COLOR, pady=15, padx=0) #Color de fondo + padding
    #root.attributes("-alpha", 0.99) #Transparencia de color


    #Página Principal
    main_frame(root)

    return root