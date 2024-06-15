import numpy as np
from particle import *

#Constants
WATER_COLOR = (0, 0, 255)
DISPERSION_RATE = 10

class Water(Particle):
    def __init__(self, row, col):
        super().__init__(row, col, WATER_COLOR, 0, True, True, .1)

    def update(self, cells):
        max_rows = len(cells)
        max_cols = len(cells[0])
        #check if the particle is movable
        if self.isMovable:
            #randomize whether it looks left or right first if it can't go down
            leftFirst = np.random.choice([True, False])
            colShift = np.random.choice([1, -1])
            #try and go down first
            if self.row+1 < max_rows and cells[self.row+1][self.col] == None:
                cells[self.row+1][self.col] = self
                cells[self.row][self.col] = None
                self.row += 1
            #try and go diagonal
            elif self.row+1 < max_rows and self.col+colShift >= 0 and self.col-colShift < max_cols and cells[self.row+1][self.col-colShift] == None:
                cells[self.row+1][self.col-colShift] = self
                cells[self.row][self.col] = None
                self.row += 1
                self.col -= colShift
            #try and go diagonal
            elif self.row+1 < max_rows and self.col-colShift >= 0 and self.col+colShift < max_cols and cells[self.row+1][self.col+colShift] == None:
                cells[self.row+1][self.col+colShift] = self
                cells[self.row][self.col] = None
                self.row += 1
                self.col += colShift
            #check left or right based on random leftShift variable and using dispersion rate
            else:
                if leftFirst:
                    for i in range(1, DISPERSION_RATE+1):
                        #Stop checking left if something other then water is detected so water doesnt just teleport
                        if self.col-i >= 0 and cells[self.row][self.col-i] is not None and cells[self.row][self.col-i] is not Water:
                            break
                        elif self.col-i >= 0 and cells[self.row][self.col-i] == None:
                            cells[self.row][self.col-i] = self
                            cells[self.row][self.col] = None
                            self.col += -i
                            break
                        elif self.col+i < max_cols and cells[self.row][self.col+i] is not None and cells[self.row][self.col+i] is not Water:
                            break
                        elif self.col+i < max_cols and cells[self.row][self.col+i] == None:
                            cells[self.row][self.col+i] = self
                            cells[self.row][self.col] = None
                            self.col += i
                            break
                else:
                    for i in range(1, DISPERSION_RATE+1):
                        #Stop checking left is something other then water is detected so water doesnt just teleport
                        if self.col+i < max_cols and cells[self.row][self.col+i] is not None and cells[self.row][self.col+i] is not Water:
                            break
                        elif self.col+i < max_cols and cells[self.row][self.col+i] == None:
                            cells[self.row][self.col+i] = self
                            cells[self.row][self.col] = None
                            self.col += i
                            break
                        elif self.col-i >= 0 and cells[self.row][self.col-i] is not None and cells[self.row][self.col-i] is not Water:
                            break
                        elif self.col-i >= 0 and cells[self.row][self.col-i] == None:
                            cells[self.row][self.col-i] = self
                            cells[self.row][self.col] = None
                            self.col += -i
                            break


