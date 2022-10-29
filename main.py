# Call files 
import KruskalAcpm
import DataStructure
import Interface
import Djikstra
import Drawing
import DisplayPcc

#create dico with the file
f = open("data/metro.txt", "r")
nodes_dico = DataStructure.init_map(f)
station_dico = DataStructure.init_station(f)
#print("There is a dico :",dico) #print all the dico data structure

#call kruskal with the dico of dico
def display_acpm():
    ACPM = KruskalAcpm.kruskal(nodes_dico)
    print('List of egdes from the ACPM of Paris metro map :', ACPM)  #print all the ACPM

#call kruskal with the dico of dico
def display_shortest_path(departure, destination):
    PCC = Djikstra.minimumPath(nodes_dico, station_dico ,departure, destination)
    print(PCC)

#display the interface
display = Interface

path = Djikstra.minimumPath(nodes_dico, station_dico, "Belleville", "Bastille")
print(path)