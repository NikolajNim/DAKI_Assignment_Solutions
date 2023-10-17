import pygame as pg
import math

pg.init() # Initialize Pygame
screen = pg.display.set_mode((1000, 1000))# Create a window of 640x480 pixels
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
width = screen.get_width()
height = screen.get_height()
center = (width / 2, height / 2)
less_center = (800, 800)
radius = 200
box_size = (25, 25)
#Draw 10 squares with loop
start_pos = (25, 25)
for j in range(8):
    for i in range(4):
        pg.draw.rect(screen, black, ((start_pos[0] + i * 50 + (25 * (j % 2)), start_pos[1] + j * 25), box_size))


for i in range(12):
    angle_rad = math.radians(i * (360/12))
    end_x = less_center[0] + radius * math.cos(angle_rad)
    end_y = less_center[1] + radius * math.sin(angle_rad)
    pg.draw.line(screen, black, less_center, (int(end_x), int(end_y)), 3)

box_pos = (0, 0)
for i in range(1, 101):
    new_box_size = (i, i)

    pg.draw.rect(screen, black, ((box_pos[0], box_pos[1]), new_box_size))
    box_pos = (box_pos[0] + new_box_size[0], box_pos[1] + new_box_size[1])

box_size = (5, 5)
angle = 5
r = 10
for i in range(500):
    rad_angle = math.radians(i * angle)
    x = r * rad_angle * math.cos(rad_angle)
    y = r * rad_angle * math.sin(rad_angle)
    pg.draw.rect(screen, black, ((center[0] + x, center[1] + y), box_size))


run_flag = True
while run_flag is True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False
    pg.display.flip() # Refresh the screen so drawing appears


    def cal_pos(center, radius, time, angle):
        angle_radian = math.radians((time - 15) * angle)
        end_x = center[0] + radius * math.cos(angle_radian)
        end_y = center[1] + radius * math.sin(angle_radian)

        return (end_x, end_y)