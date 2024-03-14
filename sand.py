import numpy as np
from particle import *

#Constants
SAND_COLOR = (194, 178, 128)

class Sand(Particle):
    def __init__(self, row, col):
        super().__init__(row, col, SAND_COLOR, 0, False, True, 1)

    def update(self, cells):
        max_rows = len(cells)
        max_cols = len(cells[0])
        #check if the particle is even movable
        if self.isMovable:
            #check if sand can even move, optimization, since currently sand can only move downwards
            if self.row+1 == max_rows:
                return
            #randomize whether it looks left or right first if it can't go down
            colShift = np.random.choice([1, -1])
            #try and go down if open
            if self.row+1 < max_rows and cells[self.row+1][self.col] is None:
                cells[self.row+1][self.col] = self
                cells[self.row][self.col] = None
                self.row += 1
            #try and go down if swappable
            elif self.row+1 < max_rows and cells[self.row+1][self.col] is not None and self.isSwappable(cells[self.row+1][self.col]):
                self.swap(cells[self.row+1][self.col], cells)
            #check diagonals based on colShift
            elif self.row+1 < max_rows and self.col+colShift >= 0 and self.col+colShift < max_cols and cells[self.row+1][self.col+colShift] is None:
                cells[self.row+1][self.col+colShift] = self
                cells[self.row][self.col] = None
                self.row += 1
                self.col += colShift
            #check same diagonal if swappable
            elif self.row+1 < max_rows and self.col+colShift >= 0 and self.col+colShift < max_cols and cells[self.row+1][self.col+colShift] is not None and  self.isSwappable(cells[self.row+1][self.col+colShift]):
                self.swap(cells[self.row+1][self.col+colShift], cells)
            elif self.row+1 < max_rows and self.col+(colShift*(-1)) >= 0 and self.col+(colShift*(-1)) < max_cols and cells[self.row+1][self.col+(colShift*(-1))] is None:
                cells[self.row+1][self.col+(colShift*(-1))] = self
                cells[self.row][self.col] = None
                self.row += 1
                self.col += colShift*(-1)
            elif self.row+1 < max_rows and self.col+(colShift*(-1)) >= 0 and self.col+(colShift*(-1)) < max_cols and cells[self.row+1][self.col+(colShift*(-1))] is not None and self.isSwappable(cells[self.row+1][self.col+(colShift*(-1))]):
                self.swap(cells[self.row+1][self.col+(colShift*(-1))], cells)




