import pygame as pg


def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)

    grid = generate_2Darray()
    grid = grid_line(grid, (1, 1), (1, 6))
    print(grid)

    visualize_grid(screen, grid)

    run_flag = True
    while run_flag:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_flag = False
        pg.display.flip()
def generate_2Darray():
    grid = []
    for i in range(48):
        column = []
        for j in range(64):
            column.append(0)
        grid.append(column)
    return grid

def grid_line(grid, start_coord, end_coord):
    x1, y1 = start_coord
    x2, y2 = end_coord

    if x1 == x2:
        for y in range(y1, y2 + 1):
            grid[y][x1] = 1
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            grid[y1][x] = 1
    else:
        raise ValueError("Only horizontal and vertical lines are supported.")

    return grid

def visualize_grid(screen, grid):
    block_size = 64  # Size of each grid block
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                pg.draw.rect(screen, (0, 0, 0), pg.Rect(x * block_size, y * block_size, block_size, block_size))
main()