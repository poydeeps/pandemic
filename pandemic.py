import pygame, random
from pygame.locals import *
from clickable import Clickable
from settings import *
from city import City
from map import Map
from deck import Deck
from card import Card

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
pygame.display.set_caption('Pandemic')
clock = pygame.time.Clock()

m = Map(list)

player_deck     = Deck(list)
player_deck.shuffle()
infection_deck  = Deck(list)
infection_deck.shuffle()

#deal player's hand
player_hand     = Deck([],'PLAYER\'S HAND')
player_deck.deal(3, player_hand)

#deal archive
archive         = Deck([],'ARCHIVE')
player_deck.deal(3, archive)


dummy_clickable=Clickable(pos=(0,0))
hovered_object = dummy_clickable

def init_screen():
    screen.blit(pygame.image.load('map.png'), (0,0))
    screen.blit(pygame.image.load('infection.png'), (968,13))
    screen.blit(pygame.image.load('outbreak.png'), (1489,429))

    player_hand.draw(screen,(1623,30))
    archive.draw(screen,(1623,200))

def check_hover():
    global hovered_object
    if not hovered_object.is_hovered():
        hovered_object = dummy_clickable
        for c in player_hand.cards + archive.cards + m.cities:
            if c.is_hovered():
                c.hover = True
                hovered_object=c
            else:
                c.hover=False

def draw_glow():
    if hovered_object.hover:
        hovered_object.draw_glow(screen)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        
#add event cards

init_screen()

crashed = False
while not crashed:

    check_hover()

    init_screen()
    draw_glow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
