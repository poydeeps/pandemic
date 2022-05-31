import pygame
from settings import *
from clickable import Clickable
from infection import Infection

class Card(Clickable):
    
    def __init__(self,**kw):
        self.pos=kw.get('pos')
        self.name=kw.get('name')
        self.color=kw.get('color')
        if 'font' in kw:
            self.font = pygame.font.SysFont(kw.get('font'), 24)
        else:
            self.font = pygame.font.SysFont(None, 24)
        self.hover=False
        self.infections = []
    
    def draw_glow(self,screen):
        x,y=self.pos
        glow_size=5
        over_surface1 = pygame.Surface((card_width+glow_size*2,card_height+glow_size*2), pygame.SRCALPHA)
        over_surface1.fill(yellow+(64,))
        pygame.draw.rect(over_surface1,yellow+(128,),pygame.Rect(glow_size/2, glow_size/2, card_width+glow_size, card_height+glow_size))
        over_surface1.set_colorkey(black)
        pygame.draw.rect(over_surface1,black,pygame.Rect(glow_size, glow_size, card_width, card_height))

        screen.blit(over_surface1,(x-glow_size,y-glow_size))

    def draw(self,screen):
        x,y=self.pos
        self.shape=pygame.Rect(x, y, card_width, card_height)
        pygame.draw.rect(screen,white,self.shape)
        pygame.draw.rect(screen,self.color,pygame.Rect(x+1, y+1, card_width-2, card_height-2))
        text = self.font.render(self.name, True, white)
        outline = self.font.render(self.name, True, black)
        screen.blit(outline, (x+10,y+10))
        screen.blit(outline, (x+12,y+10))
        screen.blit(outline, (x+11,y+9))
        screen.blit(outline, (x+11,y+11))
        screen.blit(text, (x+11,y+10))

        #offset = 2*infection_size
        #cpt = 0
        for inf in self.infections:
            #cpt+=1
            #inf.color = self.color
            #inf.pos = (x+card_width + (offset * cpt),y+(card_height/2))
            inf.draw(screen)

    def add_infection(self):
        x,y=self.pos
        x += card_width + 2*infection_size*len(self.infections)
        y += (card_height/2)
        self.infections.append(Infection(color=self.color, pos=(x,y)))

    def set_pos(self,pos):
        self.pos=pos
        x,y=pos
        x += card_width
        y += (card_height/2)

        i=0
        for inf in self.infections:
            i+=1
            x += 4*infection_size
            inf.pos = (x,y)

    def is_hovered(self):
        return self.shape.collidepoint(pygame.mouse.get_pos())