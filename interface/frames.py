from settings import(
    APP_WIDTH,
    APP_HEIGHT,
    APP_MAIN_IMAGE,
    APP_LOGO,
    APP_DESCRIPTION,
    BACKGROUND_COLOR2,
    BTN_TEXT_NEXT,
    BTN_TEXT_BACK,
    BTN_TEXT_FINISH,
    BTN_TEXT_MENU_OPTION_1,
    BTN_TEXT_MENU_OPTION_2,
    OPTION_2_TITLE,
    OPTION_2_CHECKBOX_1,
    OPTION_2_CHECKBOX_2,
    MINECRAFT_MODS_PATH,
    MINECRAFT_SHADERS_PATH,
    SHADERS_FOLDER_ID,
    MODLOADER_FOLDER_ID,
    MODLOADER_FOLDER_PATH,
    SERVER_PROPS_ID
    )
import tkinter as tk
from tkinter import font, ttk
from PIL import ImageTk, Image
from api.local_handler import LocalHandler
from api.cloud_handler import GoogleDriveHandler
import json
from utils import copy_to_clipboard, get_width_root, execute_file



#Página principal
def main_frame(root):
    page = tk.Frame(root)
    page.configure(width=APP_WIDTH, height=APP_HEIGHT, bg=root.cget('bg'))
    page.pack(fill=tk.BOTH, expand=True)

    #Título
    image = Image.open(APP_LOGO)
    width, height = image.size
    resized_image = image.resize((int(width / 1.5), int(height / 1.5)), Image.LANCZOS)
    page.tk_image = ImageTk.PhotoImage(resized_image)
    label_title = tk.Label(page, image=page.tk_image)
    label_title.configure(bd=0, bg=page.cget('bg'))
    label_title.pack()

    #Imagen a la izquierda
    left_image = Image.open(APP_MAIN_IMAGE)
    width, height = left_image.size
    resized_image = left_image.resize((int(width / 2.5), int(height / 2.5)), Image.LANCZOS)
    page.tk_left_image = ImageTk.PhotoImage(resized_image)
    label_left_image = tk.Label(page, image=page.tk_left_image)
    label_left_image.configure(bd=0)
    label_left_image.pack(side="left", fill="both")


    #Descripción
    label_description = tk.Label(page, text=APP_DESCRIPTION, justify="left", wraplength=400)
    label_description.configure(bd=0, font=("Consolas", 12))
    label_description.pack(side="right", expand=True, fill="both")

    #Segmento Botones
    button_frames = tk.Frame(label_description)
    button_frames.configure(bd=0, padx=10, pady=5)
    button_frames.pack(side="bottom", fill="x")

    def btn_continue_on_click():
        page.destroy()
        menu_frame(root)

    #Botón continuar
    btn_continue = tk.Button(button_frames, text=BTN_TEXT_NEXT, command=btn_continue_on_click)
    btn_continue.configure(padx=5, pady=5, bg="black", fg="white")
    btn_continue.pack(side="right")



#Menú de opciones
def menu_frame(root):
    page = tk.Frame(root)
    page.configure(width=APP_WIDTH, height=APP_HEIGHT, bg=root.cget('bg'))
    page.pack(fill=tk.BOTH, expand=True)

    def option_1_on_click():
        path_file = GoogleDriveHandler.download_file(MODLOADER_FOLDER_ID, MODLOADER_FOLDER_PATH)
        execute_file(path_file)

    def option_2_on_click():
        page.destroy()
        mods_frame(root)


    #Opción 1
    btn_text_menu_option_1 = tk.Button(page, text=BTN_TEXT_MENU_OPTION_1, command=option_1_on_click)
    btn_text_menu_option_1.configure(state="normal", padx=30, pady=5, bg="black", fg="white")
    btn_text_menu_option_1.pack(expand=True, pady=(0, 5))
    #Opción 2
    btn_text_menu_option_2 = tk.Button(page, text=BTN_TEXT_MENU_OPTION_2, command=option_2_on_click)
    btn_text_menu_option_2.configure(padx=30, pady=5, bg="black", fg="white")
    btn_text_menu_option_2.pack(expand=True, pady=(0, 5))


    #Segmento Botones
    button_frames = tk.Frame(page)
    button_frames.configure(bd=0, padx=10, pady=5, bg=page.cget('bg'))
    button_frames.pack(side="bottom", fill="x")

    def btn_exit_on_click():
        page.destroy()
        main_frame(root)

    #Botón salir
    btn_exit = tk.Button(button_frames, text=BTN_TEXT_BACK, command=btn_exit_on_click)
    btn_exit.configure(padx=20, pady=5, bg="black", fg="white")
    btn_exit.pack(side="right")




#Confirmar instalación de mods
def mods_frame(root):
    page = tk.Frame(root)
    page.configure(width=APP_WIDTH, height=APP_HEIGHT, bg=root.cget('bg'))
    page.pack(fill=tk.BOTH, expand=True)


    #Título
    label_title = tk.Label(page, text=OPTION_2_TITLE, justify="center", wraplength=400)
    label_title.configure(bd=0, font=("Consolas", 12), bg=page.cget('bg'), fg="white", pady=20)
    label_title.pack(side="top")


    #Contenedor de listas
    list_container = tk.Frame(page)
    list_container.pack()

    #Lista de mods faltantes
    missing_files_frame = tk.LabelFrame(list_container, text="mods faltantes")
    missing_files_frame.configure(width=300, height=200)
    missing_files_frame.pack(side="left")

    missing_files_list = tk.Listbox(missing_files_frame)
    missing_files = LocalHandler.get_missing_files()
    LocalHandler.insert_tkinter_list(missing_files_list, missing_files)
    missing_files_list.pack()

    #Lista de mods sobrantes
    excess_files_frame = tk.LabelFrame(list_container, text="mods sobrantes")
    excess_files_frame.configure(width=300, height=200)
    excess_files_frame.pack(side="left")

    excess_files_list = tk.Listbox(excess_files_frame)
    excess_files = LocalHandler.get_excess_files()
    LocalHandler.insert_tkinter_list_2(excess_files_list, excess_files)
    excess_files_list.pack()


    #Segmento de checkboxs
    radio_frames = tk.Frame(page)
    radio_frames.configure(bd=0, padx=10, pady=20, bg=page.cget('bg'), width=500, height=500)
    radio_frames.pack(fill="x")
    radio_control = tk.IntVar(value=1)

    #Checkbox 1
    radio_btn_1 = tk.Radiobutton(radio_frames, text=OPTION_2_CHECKBOX_1, variable=radio_control, value=1, anchor='w')
    radio_btn_1.configure(bd=0, pady=5)
    radio_btn_1.pack()

    #Checkbox 2
    radio_btn_2 = tk.Radiobutton(radio_frames, text=OPTION_2_CHECKBOX_2, variable=radio_control, value=2, anchor='w')
    radio_btn_2.configure(bd=0, pady=5)
    radio_btn_2.pack()

    def execute_installation():
        #Iniciar barra de progreso
        progress_bar.start()

        #Instalar mods faltantes
        GoogleDriveHandler.download_files(missing_files, MINECRAFT_MODS_PATH, progress_bar, root)
        #Instalar shaders
        shaders = GoogleDriveHandler.search_files(SHADERS_FOLDER_ID)
        GoogleDriveHandler.download_files(shaders, MINECRAFT_SHADERS_PATH, progress_bar, root)

        #Eliminar mods innecesarios
        if radio_control.get() == 1:
            LocalHandler.move_files(excess_files)
        #Mover mods innecesarios
        elif radio_control.get() == 2:
            LocalHandler.delete_files(excess_files)

        #Parar barra de progreso
        progress_bar.stop()

        page.destroy()
        final_frame(root)


    #Barra de progreso
    progress_bar = ttk.Progressbar(page, orient="horizontal", length=get_width_root())
    progress_bar.pack(side="bottom")


    #Botón confirmar
    btn_confirm = tk.Button(page, text=BTN_TEXT_NEXT, command=execute_installation)
    btn_confirm.configure(bd=0, bg="green", fg="white", pady=5, padx=5)
    btn_confirm.pack()


def final_frame(root):
    page = tk.Frame(root)
    page.configure(width=APP_WIDTH, height=APP_HEIGHT, bg=root.cget('bg'))
    page.pack(fill=tk.BOTH, expand=True)


    #Título
    label_title = tk.Label(page, text="Proceso de instalación finalizado", justify="center", wraplength=400)
    label_title.configure(bd=0, font=("Consolas", 12), bg=page.cget('bg'), fg="white", pady=20)
    label_title.pack(side="top")

    #Frame contenedor
    main_frame = tk.Frame(page)
    main_frame.configure(bd=0, padx=10, pady=5)
    main_frame.pack(expand=True, fill="both")

    #Descripción
    label_description = tk.Label(main_frame, text="Se han instalado todas las dependencias requeridas", justify="left", wraplength=400)
    label_description.configure(bd=0, font=("Consolas", 12))
    label_description.pack(expand=True, fill="both")

    #Frame contenedor de info del server
    server_props_frame = tk.Frame(main_frame)
    server_props_frame.configure(bd=0, padx=10, pady=20)
    server_props_frame.pack()

    #Datos del servidor de minecraft
    server_props = GoogleDriveHandler.download_server_props_json(SERVER_PROPS_ID)
    server_data = json.loads(server_props)
    label_ip_address = tk.Label(server_props_frame, text=f'IP: {server_data["ip_address"]}', font=font.Font(weight="bold"))
    label_ip_address.pack(side="left")

    button_copy = tk.Button(server_props_frame, command=lambda: copy_to_clipboard(server_props_frame, server_data["ip_address"]), text="copiar")
    button_copy.configure(bg="blue", fg="white")
    button_copy.pack(side="left")


    #Segmento Botones
    button_frames = tk.Frame(page)
    button_frames.configure(bd=0, padx=10, pady=5, bg=page.cget('bg'))
    button_frames.pack(side="bottom", fill="x")

    def btn_exit_on_click():
        page.destroy()
        root.destroy()

    #Botón salir
    btn_exit = tk.Button(button_frames, text=BTN_TEXT_FINISH, command=btn_exit_on_click)
    btn_exit.configure(padx=20, pady=5, bg="green", fg="white")
    btn_exit.pack(side="right")