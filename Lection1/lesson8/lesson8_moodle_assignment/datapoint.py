import pygame as pg
class Datapoint:
    def __init__(self, x, y, label, color):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), 5)
