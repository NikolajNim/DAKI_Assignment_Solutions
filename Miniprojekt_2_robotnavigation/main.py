import random
import pygame as pg
import collections as col
from queue import PriorityQueue
import a_star

def draw_tiles(screen, cost_grid):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)

    for x in range(int(height/box_size[0])):
        for y in range(int(width/box_size[1])):
            box_pos = (x * box_size[0], y * box_size[1])

            if cost_grid[x][y] == 0:
                pg.draw.rect(screen, (0,177,0), (box_pos, box_size))
            elif cost_grid[x][y] == 1:
                pg.draw.rect(screen, (4,99,4), (box_pos, box_size))
            elif cost_grid[x][y] == 5:
                pg.draw.rect(screen, (0, 100, 255), (box_pos, box_size))
            else:
                pg.draw.rect(screen, (117,150,117), (box_pos, box_size))
            pg.draw.rect(screen, (0, 0, 0), (box_pos, box_size), 1)

def cost(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    cost_list = []
    for x in range(int(height / box_size[0])):
        cost_list.append([])
        for y in range(int(width / box_size[1])):
            costs = [0,1,5,1000]
            cost_list[x].append(random.choice(costs))

    return cost_list

def node_grid(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    node_list = []
    for x in range(0, width, box_size[0]):
        for y in range(0, height, box_size[1]):
            node_list.append((x + box_size[0]/2, y + box_size[1]/2))

    return node_list


def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    cost_grid = cost(screen)
    draw_tiles(screen, cost_grid)
    nodes = node_grid(screen)
    astar = a_star.AStar(nodes)
    player_pos, goal_pos = astar.draw_champ_n_goal(screen, cost_grid)
    #print(cost_grid)
    came_from, cost_so_far = astar.a_star_search(cost_grid, nodes, player_pos, goal_pos)
    #print(nodes)
    path = astar.reconstruct(came_from, player_pos, goal_pos)
    #print(path)
    pg.draw.lines(screen, white, False, path, 2)
    print(f"cost do far: {cost_so_far}")
    #print(player_pos, goal_pos)






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

