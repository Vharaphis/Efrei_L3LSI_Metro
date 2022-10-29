#imports for the display
from cProfile import label
from sqlite3 import Row
from tkinter import *
from turtle import back, title, width
from webbrowser import get

#import main file to call different functions
import main

#create a window
window = Tk()

#define parameters for the display
window.title("Metro Boulot Dodo | Benjamin HOANG - Clément LUC - François MUTTI - Yani SADKI | LSI2")
window.geometry("1380x1000")
window.minsize(500, 500)
window.iconbitmap("data/metro.ico")
window.config(background='#38B99C')

#create menu
menu_bar = Menu(window)
#create options in the menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#add menu to the window
window.config(menu=menu_bar)

#create frames
menu_frame = Frame(window, bg='#38B99C')
menu_frame_departure = Frame(menu_frame, bg='#38B99C')
menu_frame_destination = Frame(menu_frame, bg='#38B99C')
map_frame = Frame(window, bg='#8DE3D0')

#add title
main_title = Label (menu_frame, text="Bienvenue sur l'application", font=("Courrier", 11), bg='#38B99C')
main_title.pack(side='top', pady=30)

#call the djikstra algo to determine shortest path
def submit_path():
    departure_input = departure_var.get()
    destination_input = destination_var.get()

    main.display_shortest_path(departure_input,destination_input)

    departure_var.set("")
    destination_var.set("")

departure_var = StringVar()
destination_var = StringVar()

#add text field for departure station and destination station
departure = Label(menu_frame_departure, text="Choisissez la station de départ :", bg='#38B99C')
departure.pack(side='left')
departure_entry = Entry(menu_frame_departure, textvariable=departure_var, bg='#8DE3D0')
departure_entry.pack(side='right')

destination = Label(menu_frame_destination, text="Choisissez la station de départ :", bg='#38B99C')
destination.pack(side='left')
destination_entry = Entry(menu_frame_destination, textvariable=destination_var, bg='#8DE3D0')
destination_entry.pack(side='right')

#add buttons to submit entries in departure and destination + to show the ACPM
acpm_button = Button(menu_frame, text="Afficher l'ACPM", font=("Courrier", 8), bg="#8DE3D0", command=main.display_acpm)
acpm_button.pack(side='bottom', pady=30)
djikstra_button = Button(menu_frame, text="Calculer le temps de trajet", font=("Courrier", 8), bg="#8DE3D0", command=submit_path)
djikstra_button.pack(side='bottom', pady=10)

#add the map of the metro image
metro_map_image_width = 987
metro_map_image_height = 952
metro_map_image = PhotoImage(file="data/metrof_r.png")
canvas = Canvas(map_frame, width=metro_map_image_width, height=metro_map_image_height, bg='#38B99C')
canvas.create_image(metro_map_image_width/2, metro_map_image_height/2, image=metro_map_image)
canvas.pack()

#display frames
menu_frame.pack(side='left')
menu_frame_departure.pack(side='top')
menu_frame_destination.pack(side='bottom')
map_frame.pack(side='right')

#display winodw
window.mainloop()