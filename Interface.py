#imports for the display
from cProfile import label
from tkinter import *
from turtle import back, title, width
from webbrowser import get
import Drawing
import KruskalAcpm
import DisplayPcc
#import main file to call different functions
import main
import Djikstra
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
menu_bar.add_cascade(label="Options", menu=file_menu)

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
    canvas.delete("all") #clear the previous drawing
    canvas.create_image(metro_map_image_width / 2, metro_map_image_height / 2, image=metro_map_image)
    departure_input = departure_var.get()
    destination_input = destination_var.get()

    path = Djikstra.minimumPath(main.nodes_dico, main.station_dico ,departure_input, destination_input)
    for i in range(len(path[1])-1): #draw the itinary
        a = Drawing.get_coordinate(path[1][i],main.matrix_point,main.station_dico)
        b= Drawing.get_coordinate(path[1][i+1],main.matrix_point,main.station_dico)
        canvas.create_line(int(a[0]),int(a[1]),int(b[0]),int(b[1]),fill = "black",width=5)

    itinary = DisplayPcc.read_itinary1(main.nodes_dico,main.station_dico,path)

    for widgets in frame1.winfo_children(): #clear the frame's content
        widgets.destroy()
    label = Label(frame1, text=itinary,background ='#38B99C',justify = "left")

    label.pack()
    departure_var.set("")
    destination_var.set("")

def display_ACPM():
    canvas.delete("all")
    canvas.create_image(metro_map_image_width / 2, metro_map_image_height / 2, image=metro_map_image)
    ACPM1 = KruskalAcpm.kruskal(main.nodes_dico)
    ACPM = ACPM1[0]
    for i in range(len(ACPM)):
        a = Drawing.get_coordinate(ACPM[i][0], main.matrix_point, main.station_dico)
        b = Drawing.get_coordinate(ACPM[i][1], main.matrix_point, main.station_dico)
        canvas.create_line(int(a[0]), int(a[1]), int(b[0]), int(b[1]), fill="black", width=5)

    for widgets in frame1.winfo_children():
        widgets.destroy()
    label = Label(frame1, text="Poids de l'ACPM : " + str(ACPM1[1]), background='#38B99C',font="Helvetica 14 bold")
    label.pack(side=BOTTOM)



departure_var = StringVar()
destination_var = StringVar()

#add text field for departure station and destination station
departure = Label(menu_frame_departure, text="Choisissez la station de départ :", bg='#38B99C')
departure.pack(side='left')
departure_entry = Entry(menu_frame_departure, textvariable=departure_var, bg='#8DE3D0')
departure_entry.pack(side='right')

destination = Label(menu_frame_destination, text=" Choisissez la station d'arrivée :", bg='#38B99C')
destination.pack(side='left')
destination_entry = Entry(menu_frame_destination, textvariable=destination_var, bg='#8DE3D0')
destination_entry.pack(side='right')


#add buttons to submit entries in departure and destination + to show the ACPM
acpm_button = Button(menu_frame, text="Afficher l'ACPM", font=("Courrier", 8), bg="#8DE3D0", command=display_ACPM)
acpm_button.pack(side='bottom', pady=30)
djikstra_button = Button(menu_frame, text="Calculer le temps de trajet", font=("Courrier", 8), bg="#8DE3D0", command=submit_path)
djikstra_button.pack(side='bottom', pady=10)

#exemple of input
exemple_of_entry = Label(menu_frame, text="Exemple de saisie : Bastille - Belleville", font=("Courrier", 8), bg='#38B99C')
exemple_of_entry.pack(side='bottom')

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

#display box text output

frame1 = Frame(window, background="black")
frame1.place(x=0, y=550)
#display winodw
window.mainloop()
