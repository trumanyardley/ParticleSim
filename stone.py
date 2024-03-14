from particle import *

#Constants
STONE_COLOR = (128, 128, 128)

class Stone(Particle):
    def __init__(self,row, col):
        super().__init__(row, col, STONE_COLOR, 0, False, False, 1)

    def update(self, cells):
        #stone doesn't move, currently not much else to update on
        if self.isMovable:
            pass



