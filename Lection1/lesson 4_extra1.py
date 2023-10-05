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



def draw_ball(screen, black, white, radius, start_point):
    screen.fill(white)
    pg.draw.circle(screen, black, start_point, radius)


going_down = True

i = 1
ocillate_range = height/3
run_flag = True
while run_flag is True:
    y = abs(math.sin(math.radians(i)))
    draw_ball(screen, black, white, 20, (width / 2, 600 - y * 500))
    print(abs(math.sin(math.radians(i))))
    i += 1/5


    '''
    if going_down:
        i += 1
        if i >= 500:
            going_down = False
    else:
        i -= 1 * abs(math.sin(math.radians(i)))
        if i <= 1:
            going_down = True
    '''

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False
    pg.display.flip()