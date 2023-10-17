import pygame as pg
import math
import datetime as dt

#Initializes pygame
pg.init()
screen = pg.display.set_mode((800, 800))

#Initializes a lot of colors
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 100, 100)
magenta = (255, 0, 255)
yellow = (255, 255, 0)

#Fills the pygame screen with the color white
#And Initialize useful variables
screen.fill(white)
width = screen.get_width()
height = screen.get_height()
center = (width / 2, height / 2)


#This while-loop runs until the program is terminated
run_flag = True
while run_flag is True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False

        #these if-elif chains allow the user to click the screen
        #and draw a circle with a specific color depending on which
        #region of the screen was clicked.
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pg.mouse.get_pos()

                if mouse_pos[0] <= center[0] and mouse_pos[1] <= center[1]:
                    pg.draw.circle(screen, cyan, mouse_pos, 50)

                elif mouse_pos[0] >= center[0] and mouse_pos[1] <= center[1]:
                    pg.draw.circle(screen, magenta, mouse_pos, 50)

                elif mouse_pos[0] <= center[0] and mouse_pos[1] >= center[1]:
                    pg.draw.circle(screen, yellow, mouse_pos, 50)

                elif mouse_pos[0] >= center[0] and mouse_pos[1] >= center[1]:
                    pg.draw.circle(screen, black, mouse_pos, 50)

    pg.display.flip()