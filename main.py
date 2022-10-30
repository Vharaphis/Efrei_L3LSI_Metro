# Call files 
import KruskalAcpm
import DataStructure
import Interface
import Djikstra
import Drawing
import DisplayPcc

#create dico with the file
file = open("data/metro.txt", "r")
file_2 = open("data/metro.txt", "r")
nodes_dico = DataStructure.init_map(file)
station_dico = DataStructure.init_station(file_2)
#print("There is a dico :",dico) #print all the dico data structure

#call kruskal with the dico of dico
def display_acpm():
    ACPM = KruskalAcpm.kruskal(nodes_dico)
    print('List of egdes from the ACPM of Paris metro map :', ACPM)  #print all the ACPM
    Drawing.drawing_ACPM(ACPM)

#call kruskal with the dico of dico
def display_shortest_path(departure, destination):
    PCC = Djikstra.minimumPath(nodes_dico, station_dico ,departure, destination)
    print('There is the itinary you asked :', PCC)
    DisplayPcc.read_itinary1(PCC)
    Drawing.drawing_path(PCC)

#display the interface
display = Interface
