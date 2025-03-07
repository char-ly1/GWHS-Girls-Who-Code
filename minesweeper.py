import pygame
import time
import sys

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLACK = (0, 0, 0)
WHITE = (200, 0, 0)


# def CreateBoard(BOARDSIZE):
#     pygame.init()
#     screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#              running = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 print(pygame.mouse.get_pos())
#         screen.fill("white")
#         pygame.display.flip()
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    pygame.display.flip()

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       

def drawGrid():
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            # pygame.draw.rect(SCREEN, WHITE , rect, 1)

# CreateBoard(5)
main()
