from turtle import color
import pygame, random
from pygame.locals import *
from city import City
from card import Card
from settings import *

class Deck:
    def __init__(self, list, name=False):
        self.cards  = []
        self.name   = name
        for city in list:
            #self.cards.append(City(city[0],city[1],city[2]))
            self.cards.append(Card(name=city[0],color=city[1],pos=city[2]))

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

