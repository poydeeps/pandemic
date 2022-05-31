import pygame
from settings import *

class Infection:
    def __init__(self,**kw):
        self.pos=kw.get('pos')
        self.color=kw.get('color')

    def draw(self, screen):
        x,y = self.pos
        pygame.draw.circle(screen, black, self.pos, infection_size * 1.3)
        pygame.draw.line(screen,self.color,(x,y-infection_size/2), (x+infection_size/2,y),3)
        pygame.draw.line(screen,self.color,(x,y-infection_size/2), (x-infection_size/2,y),3)
        pygame.draw.line(screen,self.color,(x,y+infection_size/2), (x+infection_size/2,y),3)
        pygame.draw.line(screen,self.color,(x,y+infection_size/2), (x-infection_size/2,y),3)
