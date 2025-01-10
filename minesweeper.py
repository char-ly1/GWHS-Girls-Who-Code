import pygame

def findSurroundingBombs(arr, row, col):
    life = 0 

    if( row >0 and arr[row -1][col] == 1):
        life += 1
    if( row < arr.length -1 and arr[row +1][col] == 1):
        life += 1
    if( col < arr[0].length -1 and arr[row][col +1] == 1):
        life += 1
    if( col > 0 and arr[row][col -1] == 1):
        life += 1
    if ( (col > 0 and row >0) and arr[row -1][col-1] == 1 ):
        life += 1
    if ( (col > 0 and row < arr.length-1) and arr[row +1][col-1] == 1 ):
        life += 1
    if ( (col < arr[0].length -1 and row < arr.length-1) and arr[row +1][col+1] == 1 ):
        life +=1
    if ( (col < arr[0].length -1 and row >0) and arr[row - 1][col+1] == 1):
        life += 1
        
    return life 

