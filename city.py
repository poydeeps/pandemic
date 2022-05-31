from turtle import Screen
import pygame
from clickable import Clickable
from infection import Infection
from settings import *
import math

class City(Clickable):
    
    def __init__(self,**kw):
        self.pos=kw.get('pos')
        self.name=kw.get('name')
        if 'color' in kw:
            self.color = kw.get('color')
        else:
            self.color=black
        if 'infections' in kw:
            self.infections = kw.get('infections')
        else:
            self.infections=[]
        self.radius = 33

    def draw(self,screen):
        cx, cy =self.pos #center of circle
        angle = 0
        for i in self.infections:
            x = cx+ (math.sin(angle) * self.radius)
            y = cy- (math.cos(angle) * self.radius)
            i.pos=(x,y)
            i.draw(screen)
            angle += 2 * math.pi/len(self.infections)


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

    def add_infection(self):
        self.infections.append(Infection(color=self.color))
