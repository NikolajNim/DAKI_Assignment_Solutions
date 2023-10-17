import random
import pygame as pg
import sys
import os

def draw_champ_n_goal(screen, cost_grid):
    red = (255, 0, 0)
    blue = (0, 0, 255)

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def draw_tiles(screen, cost_grid):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)

    font = pg.font.Font(None, 35)

    for y in range(int(height/box_size[1])):
        for x in range(int(width/box_size[0])):
            box_pos = (x * box_size[0], y * box_size[1])

            # text = font.render(f"{cost_grid[y][x]}", True, (0, 0, 0))
            # _, _, text_w, text_h = text.get_rect()
            # text_x = ((box_pos[0] + box_size[0] / 2) - text_w / 2)
            # text_y = ((box_pos[1] + box_size[1] / 2) - text_h / 2)
            # text_pos = (text_x, text_y)
            # screen.blit(text, text_pos)2
            if cost_grid[y][x] == 0:
                pg.draw.rect(screen, (0,177,0), (box_pos, box_size))
            elif cost_grid[y][x] == 1:
                pg.draw.rect(screen, (0, 100, 255), (box_pos, box_size))
            pg.draw.rect(screen, (0, 0, 0), (box_pos, box_size), 1)
def cost_grid(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    box_list = []
    for y in range(int(height / box_size[1])):
        box_list.append([])
        for x in range(int(width / box_size[0])):
            box_list[y].append(random.randint(0, 1))
    return box_list
def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    grid = cost_grid(screen)
    draw_tiles(screen, grid)


    run_flag = True
    while run_flag:

        for event in pg.event.get():
            keys = pg.key.get_pressed()

            if keys[pg.K_r]:
                main()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run_flag = False


        pg.display.flip()
if __name__ == "__main__":
    main()

