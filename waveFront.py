import numpy as np

#Este metodo me va a retornar cuales son las posiciones a las que me puedo mover desde ese punto
def perception(matrix,row,col):
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

def updateMatrix(matrix,row,col):
    perceptionArray=perception(matrix,row,col)
    #The 4 directions we can go
    up=row-1
    down=row+1
    left=col-1
    right=col+1

    #a counter to check if a movement is possible
    count=0


    #If possible,the value of the direction square will update with the current value of our square +1
    #moving up
    if(perceptionArray[0]):
        matrix[up][col]=matrix[row][col]+1
        count+=1
    #moving down
    if(perceptionArray[1]):
        matrix[down][col]=matrix[row][col]+1
        count+=1
    #Moving left
    if(perceptionArray[2]):
        matrix[row][left]=matrix[row][col]+1
        count+=1
    #Moving right:
    if(perceptionArray[3]):
        matrix[row][right]=matrix[row][col]+1
        count+=1

    #podria retornar los valores a los que fue posible moverme y en otro metodo aplicar nuevamente este metodo
    #si el metodo retorna null el algoritmo termina no olvidar EL CASO BASE
    if(count>1):
        return True
    else:
        return False





nrows=int(input("type the number of row: "))
ncols=int(input("type the numbers of columns: "))
matriz=np.zeros((nrows,ncols))
#print(type(matriz))
#print((matriz.shape)[0])

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
print(perception(matriz,rowE,colE))
updateMatrix(matriz,rowE,colE)
print(matriz)
