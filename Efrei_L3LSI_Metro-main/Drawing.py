#input file postpoint.txt
#output matrix with coordinates of all stations
def matrixe(f):
    d=[]
    for line in f:
        line = line.rstrip('\n') #delete the \n at the end of each line
        x = line.split(";")#create a tuple without ;
        d.append(x)
    return d

def get_coordinate(a,matrix_point,dico2):
    for i in range(len(matrix_point)): #
        if matrix_point[i][2]==dico2[a][0]:
            return matrix_point[i][:2]
