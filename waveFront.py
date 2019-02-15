import numpy as np

#IDEA PRINCIPAL DEL ALGORITMO, NODO FINAL REVISA HACIA DONDE SE PUEDE MOVER TENIENDO EL VECTOR DE
#POSIBILIDADES ARROJADO POR LA PERCEPCION
#UNA VEZ LO RECIBA PARA ESOS LUGARES EN LOS QUE SE PUEDE MOVER VA A ASIGNAR UN VALOR +1 DEL QUE TIENE
#CON UN METODO QUE RECIBA EL PUNTO ACTUAL Y EL VECTOR DE POSBILIDADES,
#DONDE SEA TRUE SE VA A AUMENTAR EL VALOR´+1 Y SE LLAMARA AL METODO ACTUAL NUEVAMENTE PASANDOLE EL NUEVO PUNTO Y EL VECTOR POSIBILIDADES
#E INTERNAMENTE A ESOS NUEVOS NODOS TAMBIEN SE LES VA A APLICAR 


#Este metodo me va a retornar cuales son las posiciones a las que me puedo mover desde ese punto
def perception(row,col,matrix):
    #first position stands for the possibility of moving up
    #Second for down, third position for left and fourth for right
    array=np.array([False,False,False,False])
    #the maximun potitions of the matrix
    superiorBorder=0
    inferiorBorder=((matrix.shape)[1])-1
    leftBorder=0
    rightBorder=((matrix.shape)[0])-1
    
    #The 4 directions we can go
    up=row-1
    down=row+1
    left=col-1
    right=col+1
    

    ####################TAMPOCO DEBERIA PODERSE SI YA HAY UN VALOR ASIGNADO ES DECIR SOLO TRUE CUANDO SEA 0
    #Y EVITO ´PONER LA CONDICION DEL MENOS1
    #Checks if  moving up will cause overflowing if not he will check if there is an obstacle
    #if no obstacle is found it'll make the  movement posible
    if(up>=superiorBorder): #Check for overflowing
        if(matrix[up][col]==0): #Check for obstacle
            array[0]=True

    if(down<=inferiorBorder): 
        if(matrix[down][col]==0):
            array[1]=True    

    if(left>=leftBorder):
        if(matrix[row][left]==0):
            array[2]=True

    if(right<=rightBorder):
        if(matrix[row][right]==0):
            array[3]=True
    return array




nrows=int(input("type the number of row: "))
ncols=int(input("type the numbers of columns: "))
matriz=np.zeros((nrows,ncols))
print(type(matriz))
print((matriz.shape)[0])

print("------Obstacles Allocation---------")
obstacle=True
while(obstacle==True):
    obstacleRow=int(input("type the row of the obstacle: "))
    obstacleCol=int(input("type the column of the obstacle: "))
    matriz[obstacleRow][obstacleCol]=-1
    option=input("do you want to add one more obstacle?? y/n: ")
    if(option!="y"):
        obstacle=False

print("------Start point------")
rowS=int(input("row of start point----->"))
colS=int(input("col of start point----->"))

print("------End point------")
rowE=int(input("row of End point----->"))
colE=int(input("col of End point----->"))
matriz[rowE][colE]=1
print(matriz)
print(perception(0,0,matriz))