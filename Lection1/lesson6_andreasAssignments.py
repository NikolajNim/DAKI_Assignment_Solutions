import math
import random

import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 800))
white = (255, 255, 255)
black = (0, 0, 0)
width = screen.get_width()
height = screen.get_height()
center = (width/2, height/2)
screen.fill(white)
x = center[0]
y = center[1]
v = 1
box_pos = center
box_size = (50, 50)
direction = (0, 0)

nugget_r = 25
nuggets = []
for i in range(10):
    nuggets.append((random.randrange(nugget_r, width - nugget_r), random.randrange(nugget_r, width - nugget_r)))

print(nuggets)
def draw_rect(screen, black, box_size, box_pos):
    pg.draw.rect(screen, black, (box_pos, box_size))



run_flag = True
while run_flag is True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        direction = (0, -v)
    if keys[pg.K_s]:
        direction = (0, v)
    if keys[pg.K_a]:
        direction = (-v, 0)
    if keys[pg.K_d]:
        direction = (v, 0)

    if x >= width:
        x = 0
    elif x <= 0:
        x = width
    if y >= height:
        y = 0
    elif y <= 0:
        y = height

    x += direction[0]
    y += direction[1]
    ship_pos = (x, y)
    screen.fill(white)

    nugget_removal = []
    for id, nugget in enumerate(nuggets):
        dist = math.sqrt((nugget[0] - (ship_pos[0] + box_size[0]/2))**2 - (nugget[1] - (ship_pos[1] + box_size[1]/2)**2))
        if dist < nugget_r + box_size[0]/2:
            nugget_removal.append(id)
    for nugget_id in nugget_removal:
        nuggets.pop(nugget_id)

    for nugget in nuggets:
        pg.draw.circle(screen, (255, 255, 0), nugget, nugget_r)
    draw_rect(screen, black, box_size, (x - box_size[0] / 2, y - box_size[1] / 2))

        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_w:
        #         box_pos[1] -= 10
        #     if event.key == pg.K_s:
        #         box_pos[1] += 10
        #     if event.key == pg.K_d:
        #         box_pos[0] += 10
        #     if event.key[0] == pg.K_a:
        #         box_pos[0] -= 10
    pg.display.flip()
