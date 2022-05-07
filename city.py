from turtle import Screen
import pygame
from clickable import Clickable
from settings import *

class City(Clickable):
    
    def __init__(self,**kw):
        self.pos=kw.get('pos')
        self.name=kw.get('name')
        self.color=kw.get('color')
        if 'nb_infections' in kw:
            self.nb_infections = kw.get('nb_infections')
        else:
            self.nb_infections=0
        self.radius = 33

    def draw(self,screen):
        pass

    def draw_glow(self,screen):
        glow_size = 5
        x,y=self.pos
        over_surface1 = pygame.Surface(((self.radius+glow_size)*2,(self.radius+glow_size)*2), pygame.SRCALPHA)
        pygame.draw.circle(over_surface1,yellow+(64,),(self.radius+glow_size,self.radius+glow_size),self.radius+glow_size,glow_size)
        pygame.draw.circle(over_surface1,yellow+(128,),(self.radius+glow_size,self.radius+glow_size),self.radius+glow_size,glow_size//2)

        screen.blit(over_surface1,(x-glow_size-self.radius,y-glow_size-self.radius))

    def is_hovered(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        x, y = self.pos
        return (x-x_mouse)**2 + (y-y_mouse)**2 <= self.radius ** 2
