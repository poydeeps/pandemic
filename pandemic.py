import pygame, random
from pygame.locals import *
from clickable import Clickable
from rulebook import Rulebook
from settings import *
from city import City
from deck import Deck
#from card import Card

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
pygame.display.set_caption('Pandemic')
clock = pygame.time.Clock()

game = Rulebook(screen)

#deal player's hand

game.draw_pile.deal(3, game.player_hand)

#deal archive
game.draw_pile.deal(3, game.archive)


hovered_object=Clickable(pos=(0,0))

def check_hover():
    global hovered_object
    if not hovered_object.is_hovered():
        hovered_object=Clickable(pos=(0,0))
        for c in game.player_hand.cards + game.archive.cards + game.map.cities:
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

def execute_action():
    game.next_move()
    game.execute_action()

#add event cards
game.start()

crashed = False
while not crashed:

    #init_screen()
    game.display()

    if game.phase == 'round':
        check_hover()
        draw_glow()

    if game.phase == 'setup':
        #display drawn card + infections
        game.drawn_cards.show(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            execute_action()


    pygame.display.update()
    clock.tick(15)

pygame.quit()
