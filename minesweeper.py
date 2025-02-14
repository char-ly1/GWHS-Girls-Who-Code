import pygame

def find_surrounding_bombs(arr, row, col):
    bomb_count = 0 


    if row > 0 and arr[row - 1][col] == 1:
        bomb_count += 1
    if row < len(arr) - 1 and arr[row + 1][col] == 1:
        bomb_count += 1
    if col < len(arr[0]) - 1 and arr[row][col + 1] == 1:
        bomb_count += 1
    if col > 0 and arr[row][col - 1] == 1:
        bomb_count += 1
    if col > 0 and row > 0 and arr[row - 1][col - 1] == 1:
        bomb_count += 1
    if col > 0 and row < len(arr) - 1 and arr[row + 1][col - 1] == 1:
        bomb_count += 1
    if col < len(arr[0]) - 1 and row < len(arr) - 1 and arr[row + 1][col + 1] == 1:
        bomb_count += 1
    if col < len(arr[0]) - 1 and row > 0 and arr[row - 1][col + 1] == 1:
        bomb_count += 1
        
    return bomb_count

