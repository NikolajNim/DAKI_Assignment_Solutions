import pygame as pg
import math
import datetime as dt

pg.init()
screen = pg.display.set_mode((800, 800))
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
width = screen.get_width()
height = screen.get_height()
center = (width / 2, height / 2)




#Allows object to move every second
def rotate_line(center : tuple, length):
    second = dt.datetime.now().second
    angle = 360/60
    rad_angle = math.radians(second * angle)
    x = center[0] + length * math.cos(rad_angle)
    y = center[1] + length * math.sin(rad_angle)

    return (x, y)

#Draws the line right after refreashing the s
def draw_line(screen, center, length, white, black):
    screen.fill(white)
    pg.draw.line(screen, black, center, rotate_line(center, length), 2)


run_flag = True
while run_flag is True:
    draw_line(screen, center, 100, white, black)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False
    pg.display.flip()