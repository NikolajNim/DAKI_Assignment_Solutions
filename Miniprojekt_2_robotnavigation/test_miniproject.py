import  pygame as pg
import random
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

def color_picker(rand_num):
    if rand_num == 1:
        return (0, 177, 0)
    elif rand_num == 2:
        return (4, 99, 4)
    elif rand_num == 5:
        return (0, 100, 255)
    else:
        return (20, 20, 20)

def node_grid(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    node_list = []
    cost_list = []
    for x in range(0, width, box_size[0]):
        for y in range(0, height, box_size[1]):
            #print(x, y)
            node_list.append((x, y))
            costs = [1, 2, 5, 10000]
            random_choice = random.choice(costs)
            box_pos = (x, y)
            pg.draw.rect(screen, color_picker(random_choice), (box_pos, box_size))
            pg.draw.rect(screen, (0, 0, 0), (box_pos, box_size), 1)

            cost_list.append(random_choice)

    return node_list, cost_list