import random
from copy import deepcopy

import pygame as pg


def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)

    grid = generate_2Darray(size=(64, 48))
    print(grid)
    for x in range(0, 64, 2):
        split_pos = random.randrange(1, 48)
        grid = grid_line(grid, (x, 0), (x, split_pos-1))
        grid = grid_line(grid, (x, split_pos+1), (x, 48-1))


    visualize_grid(screen, grid)

    run_flag = True
    while run_flag:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_flag = False
        pg.display.flip()

def generate_2Darray(size=(64, 48)):
    grid = []
    for i in range(size[1]):
        grid.append([])
        for j in range(size[0]):
            grid[i].append(0)
    return grid

def grid_line(grid, start_coord, end_coord):
    assert(start_coord[0] == end_coord[0] or start_coord[1] == end_coord[1])
    grid = deepcopy(grid)
    if start_coord[1] == end_coord[1]:
        for x in range(start_coord[0], end_coord[0]+1):
            grid[start_coord[1]][x] = 1
    else:
        for y in range(start_coord[1], end_coord[1]+1):
            grid[y][start_coord[0]] = 1
    return grid


    # x1, y1 = start_coord
    # x2, y2 = end_coord
    #
    # if x1 == x2:
    #     for y in range(y1, y2 + 1):
    #         grid[y][x1] = 1
    # elif y1 == y2:
    #     for x in range(x1, x2 + 1):
    #         grid[y1][x] = 1
    # else:
    #     raise ValueError("Only horizontal and vertical lines are supported.")


def visualize_grid(screen, grid, block_size=10):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 1:
                pg.draw.rect(screen, (0, 0, 0),(x * block_size, y * block_size, block_size, block_size))


    # for y in range(len(grid)):
    #     for x in range(len(grid[0])):
    #         if grid[y][x] == 1:
    #             pg.draw.rect(screen, (0, 0, 0), pg.Rect(x * block_size, y * block_size, block_size, block_size))
main()