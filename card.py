import pygame
from settings import *
from clickable import Clickable

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

    def is_hovered(self):
        return self.shape.collidepoint(pygame.mouse.get_pos())