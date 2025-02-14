import pygame

class Minesweeper:
    

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
    
def main():
    game = Minesweeper()
    center_bomb_count = game.find_surrounding_bombs(1, 1)  # Check surrounding bombs at (1,1)
    print("Bombs around center:", center_bomb_count)


if __name__ == "__main__":
    main()
