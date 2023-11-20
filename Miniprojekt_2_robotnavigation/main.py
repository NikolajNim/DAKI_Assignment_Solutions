import random
import pygame as pg
import collections as col
from queue import PriorityQueue
import a_star
import test_miniproject

# def draw_tiles(screen, cost_grid):
#     width = screen.get_width()
#     height = screen.get_height()
#     box_size = (25, 25)
#
#     for x in range(int(height/box_size[0])):
#         for y in range(int(width/box_size[1])):
#             box_pos = (x * box_size[0], y * box_size[1])
#
#             if cost_grid[x][y] == 0:
#                 pg.draw.rect(screen, (0,177,0), (box_pos, box_size))
#             elif cost_grid[x][y] == 1:
#                 pg.draw.rect(screen, (4,99,4), (box_pos, box_size))
#             elif cost_grid[x][y] == 5:
#                 pg.draw.rect(screen, (0, 100, 255), (box_pos, box_size))
#             else:
#                 pg.draw.rect(screen, (10,10,10), (box_pos, box_size))
#             pg.draw.rect(screen, (0, 0, 0), (box_pos, box_size), 1)
#
# def cost(screen):
#     width = screen.get_width()
#     height = screen.get_height()
#     box_size = (25, 25)
#     cost_list = []
#     for x in range(int(height / box_size[0])):
#         cost_list.append([])
#         for y in range(int(width / box_size[1])):
#             costs = [0,1,5,1000]
#             cost_list[x].append(random.choice(costs))
#
#     return cost_list
#
# def node_grid(screen):
#     width = screen.get_width()
#     height = screen.get_height()
#     box_size = (25, 25)
#     node_list = []
#     for x in range(0, width, box_size[0]):
#         for y in range(0, height, box_size[1]):
#             node_list.append((x + box_size[0]/2, y + box_size[1]/2))
#
#     return node_list

def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    screen.fill(white)
    nodes, cost_grid = test_miniproject.node_grid(screen)
    # cost_grid = cost(screen)
    # draw_tiles(screen, cost_grid)
    # nodes = node_grid(screen)

    astar = a_star.AStar(nodes)
    player_pos, goal_pos = astar.draw_champ_n_goal(screen, nodes)
    came_from, cost_so_far = astar.a_star_search(cost_grid, nodes, player_pos, goal_pos)
    print(f"Cost so far: {cost_so_far}")
    path = astar.reconstruct(came_from, player_pos, goal_pos)
    print(f"path: {path}")
    new_path = [(x + 12.5, y + 12.5) for x, y in path]
<<<<<<< HEAD
    print(new_path)
=======

    # print(cost_grid)
    # print(nodes)
    #print(path)
    # #print(new_path)
>>>>>>> 100c07e4caea685edb4fc399094a8903b54b401c
    # for i in enumerate(path):
    #     popped = path.pop(i)
    #     new_point = (popped[0] + 12.5, popped[1] + 12.5)
    #     path.append(new_point)
    # print(path)
    pg.draw.lines(screen, white, False, new_path, 3)
    #print(f"cost do far: {cost_so_far}")
    #print(player_pos, goal_pos)
    #print(random.choice(nodes))
    #print(cost_grid[0])
<<<<<<< HEAD
    #print(nodes)
    #print(cost_grid)
=======
    # print(nodes)
    # print(cost_grid)
>>>>>>> 100c07e4caea685edb4fc399094a8903b54b401c


    # nodes1, cost_grid1 = test_miniproject.node_grid1(screen)
    # # cost_grid = cost(screen)
    # # draw_tiles(screen, cost_grid)
    # # nodes = node_grid(screen)
    # astar1 = a_star.AStar(nodes1)
    # player_pos1, goal_pos1 = astar1.draw_champ_n_goal(screen, nodes1)
    # came_from1, cost_so_far1 = astar1.a_star_search(cost_grid1, nodes1, player_pos1, goal_pos1)
    # path1 = astar1.reconstruct(came_from1, player_pos1, goal_pos1)
    # new_path1 = [(x + 12.5, y + 12.5) for x, y in path1]
    # # print(cost_grid)
    # # print(nodes)
    # # print(path)
    # # #print(new_path)
    # # for i in enumerate(path):
    # #     popped = path.pop(i)
    # #     new_point = (popped[0] + 12.5, popped[1] + 12.5)
    # #     path.append(new_point)
    # print(f"path: {path1}")
    # print(f"came from: {came_from1}")
    # for i in range(len(path1)):
    #     print(cost_so_far1[path1[i]])
    # pg.draw.lines(screen, white, False, new_path1, 3)
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

