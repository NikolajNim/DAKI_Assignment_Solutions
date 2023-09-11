

import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((1000, 1000))# Create a window of 640x480 pixels
white = (255.0, 255.0, 255.0)
black = (0.2, 0.2, 0.2)
width = screen.get_width()
height = screen.get_height()

screen.fill(white) # Fill the screen with white

p1 = (width/3, height/3)
p2 = (width/3, height/3*2)
p3 = (width/3*2, height/3*2)
p4 = (width/3*2, height/3)
p5 = (width/2, height/8)

points = [p1,p2,p3,p4,p5,p1,p4]

'''
pygame.draw.line(screen, black, (width/3, height/3*2), (width/3*2, height/3*2)) # Draw a black line
pygame.draw.line(screen, black, (width/3, height/3*2), (width/3, height/3))
pygame.draw.line(screen, black, (width/3*2, height/3*2), (width/3*2, height/3))
pygame.draw.line(screen, black, (width/3, height/3), (width/3*2, height/3))
pygame.draw.line(screen, black, (width/3, height/3), (width/2, height/8))
pygame.draw.line(screen, black, (width/3*2, height/3), (width/2, height/8))
'''
pygame.draw.lines(screen, black, True, points, 5)

# Draw the ground
# Draw the bottom of the house
# Draw two walls
# Draw the roof

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears