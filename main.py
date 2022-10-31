# Call files 
import KruskalAcpm
import DataStructure
import Interface
import Djikstra
import Drawing
import DisplayPcc

#create dico with the file
file = open("data/metro.txt", "r",encoding='utf-8')
file_2 = open("data/metro.txt", "r",encoding='utf-8')
file_3 = open("data/pospoints.txt","r",encoding='utf-8')
nodes_dico = DataStructure.init_map(file)
station_dico = DataStructure.init_station(file_2)
matrix_point = Drawing.matrixe(file_3)



#display the interface
display = Interface

if __name__ == '__main__':
    Drawing.drawing_ACPM(KruskalAcpm.kruskal(nodes_dico), matrix_point, station_dico)