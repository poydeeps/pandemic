import pygame, random
from pygame.locals import *
from city import City
from settings import *

class Deck:
    def __init__(self, list, name=False):
        self.cards  = []
        self.name   = name
        for city in list:
            self.cards.append(City(city[0],city[1],city[2]))
    def deal(self, nb, deck_to):
        for x in range(nb):
            card = random.choice(self.cards)
            deck_to.append(card)
            self.cards.remove(card)
    def append(self, card):
        self.cards.append(card)
    def draw_title(self, screen, x, y):
        font_size = 24
        font = pygame.font.SysFont(None, font_size)
        pygame.draw.rect(screen,white,pygame.Rect(x, y, card_width, card_height))
        pygame.draw.rect(screen,black,pygame.Rect(x+2, y+2, card_width-4, card_height-4))
        text = font.render(self.name, True, white)
        outline = font.render(self.name, True, black)
        screen.blit(outline, (x+9,y+(card_height-font_size)/2))
        screen.blit(outline, (x+11,y+(card_height-font_size)/2))
        screen.blit(outline, (x+10,y+(card_height-font_size)/2-1))
        screen.blit(outline, (x+10,y+(card_height-font_size)/2+1))
        screen.blit(text, (x+10,y+(card_height-font_size)/2))
