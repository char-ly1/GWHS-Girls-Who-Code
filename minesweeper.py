import pygame

class Minesweeper:
    
# Board is 400 x 400 according to Nicole 
    def __init__(self):
        # 3x3 grid with bombs surrounding the center
        self.grid = [
            [0, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ]


    def find_surrounding_bombs(self, row, col):
        bomb_count = 0

        if row > 0 and self.grid[row - 1][col] == 1:
            bomb_count += 1
        if row < len(self.grid) - 1 and self.grid[row + 1][col] == 1:
            bomb_count += 1
        if col < len(self.grid[0]) - 1 and self.grid[row][col + 1] == 1:
            bomb_count += 1
        if col > 0 and self.grid[row][col - 1] == 1:
            bomb_count += 1
        if col > 0 and row > 0 and self.grid[row - 1][col - 1] == 1:
            bomb_count += 1
        if col > 0 and row < len(self.grid) - 1 and self.grid[row + 1][col - 1] == 1:
            bomb_count += 1
        if col < len(self.grid[0]) - 1 and row < len(self.grid) - 1 and self.grid[row + 1][col + 1] == 1:
            bomb_count += 1
        if col < len(self.grid[0]) - 1 and row > 0 and self.grid[row - 1][col + 1] == 1:
            bomb_count += 1
            
        return bomb_count
    
    def mouse_click_to_grid(self, x, y):
        # 400 x 400 pixel grid
        # in game, 10 x 10 cell grid
        # each cell is 40 x 40 pixels
        # return cell index from 0 to 9 based on the pixel coordinates :D
        x_cor = x // 40
        y_cor = y // 40
        if(x_cor == 10):
            x_cor = 9
        if(y_cor == 10):
            y_cor = 9
        return int(x_cor), int(y_cor)
    
    def click_left_right(self):
        pygame.init()
        mouse_clicked = pygame.mouse.get_pressed()
        if mouse_clicked[0] and not mouse_clicked[1]:
            # left click, select the box
            print("Left click detected: Selecting the box.")
            
        if mouse_clicked[1] and not mouse_clicked[0]:
            # right click, flag the box
            print("Right click detected: Flagging the box.")

        if mouse_clicked[0] and mouse_clicked[1]:
            pass
        

def main():
    game = Minesweeper()
    pygame.init()
    x , y = game.mouse_click_to_grid(84, 126)
    print(f"Cell clicked: {x}, {y}")


if __name__ == "__main__":
    main()