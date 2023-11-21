import random
import numpy as np
import pygame as pg
import a_star

def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    screen.fill(white)

    matrix_size = (32, 32)
    matrix = np.random.randint(1, 5, matrix_size)

    # new_matrix = []
    # for x in range(matrix_size[0]):
    #     new_matrix.append([])
    #     for y in range(matrix_size[1]):
    #         if x % 2 == 0 and y % 2 == 0:
    #             new_matrix[x].append(4)
    #         else:
    #             new_matrix[x].append(1)
    # print(new_matrix)


    print(matrix)

    astar = a_star.Astar(matrix, matrix_size, box_size=(25, 25))
    astar.draw_grid(screen)
    a, b = astar.draw_a_b(screen)

    # for x, col in enumerate(matrix):
    #     for y, output in enumerate(col):
    #         print(x, y)

    # print(a, b)

    came_from, cost_so_far = astar.astar_search(a, b)
    print(a, b)
    path = astar.reconstruct(came_from, a, b)
    print(path)

    scaled_path = [(x * 25, y * 25) for x, y in path]
    adjusted_path = [(x + 12.5, y + 12.5) for x, y in scaled_path]

    pg.draw.lines(screen, white, False, adjusted_path, 4)

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
