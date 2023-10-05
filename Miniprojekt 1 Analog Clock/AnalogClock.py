import datetime as dt
import pygame as pg
import math

def main():
    #initializing of all the needed variables
    pg.init()  # Initialize Pygame
    screen = pg.display.set_mode((1000, 1000))
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    screen.fill(white)
    width = screen.get_width()
    height = screen.get_height()
    center = (width / 2, height / 2)
    radius = 300
    angle_step = 360 / 12
    angle_step_min = 360 / 60

    #creates lists needed for end points
    endP_list = []
    endP_min_list = []

    generate_watch_face(angle_step, angle_step_min, black, center, endP_list, endP_min_list, radius, screen, white)

    font = pg.font.Font(None, 100)
    for i in range(1, 13):
        rad_angle = math.radians(i * angle_step)
        x = center[0] + radius + 20 * math.cos(rad_angle) - 15
        y = center[1] - radius + 20 * math.sin(rad_angle) - 20
        number_text = font.render(str(i), True, black)
        text_rect = number_text.get_rect()
        text_rect.center(x, y)
        screen.blit(number_text, text_rect)

    run_flag = True
    while run_flag is True:

        watch(screen, white, center, radius - 40, red, blue, green)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_flag = False
        pg.display.flip()  # Refresh the screen so drawing appears

#This function genereates the watchface using most of the initializes variables.
def generate_watch_face(angle_step, angle_step_min, black, center, endP_list, endP_min_list, radius, screen, white):
    for i in range(60):
        angle_radian = math.radians(i * angle_step_min)
        end_x = center[0] + radius * math.cos(angle_radian)
        end_y = center[1] - radius * math.sin(angle_radian)
        endP_min_list.append((end_x, end_y))
        pg.draw.line(screen, black, center, (int(end_x), int(end_y)), 3)

    pg.draw.circle(screen, white, center, radius - 20)

    for i in range(12):
        angle_radian = math.radians(i * angle_step)
        end_x = center[0] + radius * math.cos(angle_radian)
        end_y = center[1] - radius * math.sin(angle_radian)
        endP_list.append((end_x, end_y))
        pg.draw.line(screen, black, center, (int(end_x), int(end_y)), 5)

    pg.draw.circle(screen, white, center, radius - 50)
    pg.draw.circle(screen, black, center, radius, 4)
    pg.draw.circle(screen, black, center, 4)

#This function is used to calculate the next position of a "watch hand"
#This is only used for watch hands, because of the needed time parameter
def cal_pos(center, radius, time, angle):
    angle_radian = math.radians((time - 15) * angle)
    end_x = center[0] + radius * math.cos(angle_radian)
    end_y = center[1] + radius * math.sin(angle_radian)

    return (end_x, end_y)

#This function is suppose to run in the while, because it moves the watchhands by implementing time
def watch(screen, white, center, radius, red, blue, green):
    pg.draw.circle(screen, white, center, radius +10)

    current_time = dt.datetime.now()
    microsec = current_time.microsecond
    sec = current_time.second + (microsec/1000000)
    minute = current_time.minute + (sec/6) * 0.1
    hour = current_time.hour + (minute/6) * 0.1

    pg.draw.line(screen, red, center, cal_pos(center, radius, sec, 6), 2)
    pg.draw.line(screen, blue, center, cal_pos(center, radius, minute, 6), 3)
    pg.draw.line(screen, green, center, cal_pos(center, radius - 40, hour, 30), 4)

main()