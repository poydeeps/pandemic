from turtle import color
import pygame, random
from pygame.locals import *
from city import City
from card import Card
from settings import *

class Deck:
    def __init__(self, city_list, name=False):
        self.cards  = []
        self.name   = name
        for city in city_list:
            #self.cards.append(City(city[0],city[1],city[2]))
            self.cards.append(Card(name=city[0],color=city[1],pos=city[2]))
        self.font = pygame.font.SysFont(None, 24)

    def deal(self, nb, deck_to):
        for x in range(nb):
            card = self.cards.pop(0)
            deck_to.append(card)

    def append(self, card):
        self.cards.append(card)

    def draw(self,screen,pos):
        x,y=pos
        deck_title=Card(name=self.name, color=black, pos=pos)
        deck_title.draw(screen)
        for c in self.cards:
            y+=card_height
            c.pos=(x,y)
            c.draw(screen)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def show(self,screen):
        banner = pygame.Surface((display_width,banner_height),pygame.SRCALPHA)
        banner.fill(banner_color)
        screen.blit(banner,(0,banner_y_offset))
        spacing=banner_height / (len(self.cards)+2)
        x=(display_width - card_width)/2
        y= banner_y_offset + spacing
        text = self.font.render(self.name, True, white)
        screen.blit(text, (x,y))

        for c in self.cards:
            y +=spacing
            c.set_pos((x,y))
            c.draw(screen)

    def last_card(self):
        return self.cards[-1]

