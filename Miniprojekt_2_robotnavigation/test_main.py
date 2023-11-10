import pygame as pg
import a_star
import test_miniproject
def node_grid(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    node_list = []
    for x in range(0, width, box_size[0]):
        for y in range(0, height, box_size[1]):
            node_list.append((x, y))

    return node_list
def test_main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    screen.fill(white)

    nodes = node_grid(screen)
    print(nodes)


    run_flag = True
    while run_flag:

        for event in pg.event.get():
            keys = pg.key.get_pressed()

            if keys[pg.K_r]:
                test_main()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run_flag = False
        pg.display.flip()

test_main()
