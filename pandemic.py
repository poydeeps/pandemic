import pygame, random
from pygame.locals import *
from settings import *
from city import City
from map import Map
from deck import Deck

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
pygame.display.set_caption('Pandemic')
clock = pygame.time.Clock()

m = Map(list)

player_deck     = Deck(list)
infection_deck  = Deck(list)

#deal player's hand
player_hand     = Deck([],'PLAYER\'S HAND')
player_deck.deal(3, player_hand)

#deal archive
archive         = Deck([],'ARCHIVE')
player_deck.deal(3, archive)

#add event cards

crashed = False
while not crashed:

    screen.blit(pygame.image.load('map.png'), (0,0))
    screen.blit(pygame.image.load('infection.png'), (968,13))
    screen.blit(pygame.image.load('outbreak.png'), (1489,429))

    y = 30
    player_hand.draw_title(screen, 1623, 30)
    y+=32
    for c in player_hand.cards:
        pygame.draw.rect(screen,white,pygame.Rect(1623, y-11, 277, 34))
        pygame.draw.rect(screen,c.color,pygame.Rect(1624, y-9, 273, 30))
        text = font.render(c.name, True, white)
        outline = font.render(c.name, True, black)
        screen.blit(outline, (1634,y))
        screen.blit(outline, (1636,y))
        screen.blit(outline, (1635,y-1))
        screen.blit(outline, (1635,y+1))
        screen.blit(text, (1635,y))
        y+=32

    y+=32

    pygame.draw.rect(screen,white,pygame.Rect(1623, y-11, 277, 34))
    pygame.draw.rect(screen,black,pygame.Rect(1624, y-9, 273, 30))
    text = font.render("ARCHIVE", True, white)
    outline = font.render("ARCHIVE", True, black)
    screen.blit(outline, (1634,y))
    screen.blit(outline, (1636,y))
    screen.blit(outline, (1635,y-1))
    screen.blit(outline, (1635,y+1))
    screen.blit(text, (1635,y))
    y+=32
    for c in archive.cards:
        pygame.draw.rect(screen,white,pygame.Rect(1623, y-11, 277, 34))
        pygame.draw.rect(screen,c.color,pygame.Rect(1624, y-9, 273, 30))
        text = font.render(c.name, True, white)
        outline = font.render(c.name, True, black)
        screen.blit(outline, (1634,y))
        screen.blit(outline, (1636,y))
        screen.blit(outline, (1635,y-1))
        screen.blit(outline, (1635,y+1))
        screen.blit(text, (1635,y))
        y+=32

    over = False
    city_circles = screen.copy()
    for c in m.cities:
        if pygame.draw.circle(city_circles, green, c.pos, 33, 33).collidepoint(pygame.mouse.get_pos()):
            over = True
    if over == True:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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
