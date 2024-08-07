import os
import time
from random import randint

class GameOfLife:
    
    def __init__(self, rows: int, cols: int, num_cells: int):
        self.__rows = rows
        self.__cols = cols
        self.__num_cells = num_cells
        self.__grid = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        
    def generate_random_cells(self):
        self.__grid = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        
        cells_placed = 0
        while cells_placed < self.__num_cells:
            x = randint(0, self.__rows - 1)
            y = randint(0, self.__cols - 1)
            
            if self.__grid[x][y] == 0:  
                self.__grid[x][y] = 1
                cells_placed += 1
    
    def display_matrice(self):
        for row in self.__grid:
            print(' '.join(str(cell) for cell in row))
        print()  
    
    def count_neighbors(self, x: int, y: int) -> int:
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.__rows and 0 <= ny < self.__cols:
                if self.__grid[nx][ny] == 1:
                    count += 1
        
        return count
    
    def evolve(self):
        new_grid = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        
        for x in range(self.__rows):
            for y in range(self.__cols):
                count = self.count_neighbors(x, y)
                if self.__grid[x][y] == 1:  # Cell Alive
                    if count < 2 or count > 3:
                        new_grid[x][y] = 0
                    else:
                        new_grid[x][y] = 1
                else:  # Dead Cell
                    if count == 3:
                        new_grid[x][y] = 1
        
        self.__grid = new_grid
    
    def game_of_life(self, max_generations: int, delay: float):
        self.generate_random_cells()
        self.display_matrice()
        
        for generation in range(max_generations):
            time.sleep(delay)  # slow output
            os.system('cls' if os.name == 'nt' else 'clear') 
            self.evolve()
            self.display_matrice()
    

game_of_life = GameOfLife(50, 50, 300)
game_of_life.game_of_life(500, 1) 
