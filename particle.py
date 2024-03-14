import pygame

#Constants
PARTICLE_DIMENSION = 10

class Particle:
    #Every particle has these attributes
    #Location: row,col
    #Color: color of particle
    #Velocity: current speed which will dictate how its position is updated
    #Flammable: can it catch on fire
    #Movement: is it affected by gravity
    #Density: mostly for interactions between solids and liquids (are they swappable), generally solids 1, liquids 0
    def __init__(self, row, col, color, velocity, isFlammable, isMovable, density):
        self.row = row
        self.col = col
        self.color = color
        self.velocity = velocity
        self.isFlammable = isFlammable
        self.isMovable = isMovable
        self.density = density

    #How a particle should move each step, abstract and will be determined by each particle class
    def update(self, cells):
        pass

    #How each particle is drawn to the screen
    def draw(self, screen):
        if self is not None:
            pygame.draw.rect(screen, self.color, (self.col * PARTICLE_DIMENSION, self.row * PARTICLE_DIMENSION, PARTICLE_DIMENSION, PARTICLE_DIMENSION))

    #Returns if current particle is swappable with target
    def isSwappable(self, Particle):
        return self.density > Particle.density

    def swap(self, other_particle, cells):
        row, col = self.row, self.col
        self.row, self.col = other_particle.row, other_particle.col
        other_particle.row, other_particle.col = row, col

        cells[self.row][self.col] = self
        cells[other_particle.row][other_particle.col] = other_particle
        other_particle.update(cells)




        
