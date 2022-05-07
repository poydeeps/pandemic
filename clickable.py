import pygame

class Clickable:
    def __init__(self, **kw):
        self.pos=kw.get('pos')
        self.name=kw.get('name')
        self.color=kw.get('color')
        self.hover=False

    def draw_glow(self,screen):
        pass

    def draw(self,screen):
        pass

    def is_hovered(self):
        return False