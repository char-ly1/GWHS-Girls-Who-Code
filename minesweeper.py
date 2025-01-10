import pygame
import time

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def CreateBoard(BOARDSIZE):
    pygame.init()
    screen = pygame.display.set_mode((650, 650))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             running = False
            if event.type == pygame.MOUSEBUTTONUP:
                print(pos = pygame.mouse.get_pos())
        screen.fill("white")
        pygame.display.flip()

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

CreateBoard(5)

 
