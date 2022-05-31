from infection import Infection
from map import Map
from settings import *
from deck import Deck
import pygame

class Rulebook:
    def __init__(self, screen):
        self.draw_pile     = Deck(city_list,'DRAW PILE')
        self.draw_pile.shuffle()
        self.drawn_cards = Deck([],'CITIES INFECTIONS')
        self.setup_steps = [
            ['card 1',self.deal_infection,3], #draw 1 card, place 3 infections
            ['card 2',self.deal_infection,3],
            ['card 3',self.deal_infection,2],
            ['card 4',self.deal_infection,2],
            ['card 5',self.deal_infection,1],
            ['card 6',self.deal_infection,1],
            ['place infection',self.advance_infection,1], #advance the infection token 1 spot
            ['place oubreak',self.advance_outbreak,1] #advance the outbreak token 1 spot
        ]
        self.round_steps = [
            ['draw_card',1],
            ['action'],
            ['action'],
            ['action'],
            ['action']
        ]
        self.current_step = self.setup_steps[0]
        self.phase = 'stop'
        self.screen = screen
        self.map = Map(city_list)
        self.player_hand     = Deck([],'PLAYER\'S HAND')
        self.archive         = Deck([],'ARCHIVE')
        self.outbeak_spot=0
        self.infection_spot=0

    def start(self):
        self.phase='start'

    def check_win(self):
        #to do : check the win condition
        return False

    def ckeck_lose(self):
        #to do : check the lose condition
        return False

    def next_move(self):
        if self.phase=='round':
            curpos = self.round_steps.index(self.current_step)
            nextpos = (curpos+1) % len(self.round_steps)
            self.current_step = self.round_steps[nextpos]

        if self.phase=='setup':
            curpos = self.setup_steps.index(self.current_step)
            nextpos = (curpos+1) % len(self.setup_steps)
            if nextpos == 0 :
                self.phase = 'round'
                self.current_step = self.round_steps[0]
            else :
                self.current_step = self.setup_steps[nextpos]
        if self.phase=='start':
            self.phase = 'setup'
            self.current_step = self.setup_steps[0]

    def execute_action(self):
        if self.phase=='round':
            pass
        if self.phase=='setup':
            self.current_step[1](self.current_step[2])

    def deal_infection(self, nb_infections):
        self.draw_pile.deal(1,self.drawn_cards)
        for i in range(nb_infections):
            self.drawn_cards.last_card().add_infection()
            self.map.get_city_by_name(self.drawn_cards.last_card().name).add_infection()

    def advance_outbreak(self,nb_spots):
        self.outbeak_spot+=nb_spots

    def advance_infection(self,nb_spots):
        self.infection_spot+=nb_spots

    def display(self):
        self.screen.blit(pygame.image.load('map.png'), (0,0))
        self.__display_outbreak()
        self.__display_infection()
        self.player_hand.draw(self.screen,(1623,30))
        self.archive.draw(self.screen,(1623,200))
        self.map.draw(self.screen)

    def __display_outbreak(self):
        if self.outbeak_spot > 0:
            x=1489
            y=97*self.outbeak_spot + 332
            self.screen.blit(pygame.image.load('outbreak.png'), (x,y))

    def __display_infection(self):
        if self.infection_spot > 0:
            x=82*self.infection_place + 886
            y=13
            self.screen.blit(pygame.image.load('infection.png'), (x,y))
