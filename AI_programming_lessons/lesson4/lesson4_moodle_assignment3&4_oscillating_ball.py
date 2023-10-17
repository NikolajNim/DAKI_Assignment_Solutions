import pygame as pg
import math
import datetime as dt

#Draws the ball
def draw_ball(screen, black, white, radius, start_point):
    screen.fill(white)
    pg.draw.circle(screen, black, start_point, radius)

#Initialize pygame, colors and useful variables
pg.init()
screen = pg.display.set_mode((800, 800))
white = (255, 255, 255)
black = (0, 0, 0)
width = screen.get_width()
height = screen.get_height()
center = (width / 2, height / 2)

#Uses the sine curve to make the ball oscillate up and down like a real ball
i = 1
run_flag = True
while run_flag is True:
    y = abs(math.sin(math.radians(i)))
    draw_ball(screen, black, white, 20, (width / 2, 600 - y * 500))
    #print(abs(math.sin(math.radians(i))))
    i += 1/15

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False
    pg.display.flip()