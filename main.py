# Call files 
import KruskalAcpm
import DataStructure
import Interface
import Djikstra

#create dico with the file
f = open("data/metro.txt", "r")
dico = data_structure.init_map(f)
#dico = (data_structure.init_station(f))
#print("There is a dico :",dico) #print all the dico data structure

#call kruskal with the dico of dico
def display_acpm():
    ACPM = kruskal_acpm.kruskal(dico)
    print('List of egdes from the ACPM of Paris metro map :', ACPM)  #print all the ACPM

#call kruskal with the dico of dico
def display_shortest_path(departure, destination):
    #call Djikstra
    ...

#display the interface
display = interface
