import random
import pygame as pg
import collections as col
from queue import PriorityQueue

def draw_champ_n_goal(screen, cost_grid, box_size = (25, 25)):
    red = (255, 0, 0)
    magenta = (255, 0, 255)
    width = screen.get_width()
    height = screen.get_height()
    rand_pos_x = random.randrange(len(cost_grid))
    rand_pos_y = random.randrange(len(cost_grid))

    player_box_pos = (rand_pos_x * box_size[0], rand_pos_y * box_size[1])
    pg.draw.rect(screen, red, (player_box_pos, box_size))

    goal_x = width - rand_pos_x * box_size[0] - box_size[0]
    goal_y = height - rand_pos_y * box_size[1] - box_size[1]
    goal_box_pos = (goal_x, goal_y)
    pg.draw.rect(screen, magenta, (goal_box_pos, box_size))

    return player_box_pos, goal_box_pos


def draw_tiles(screen, cost_grid):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)

    # font = pg.font.Font(None, 35)

    for x in range(int(height/box_size[0])):
        for y in range(int(width/box_size[1])):
            box_pos = (x * box_size[0], y * box_size[1])

            # text = font.render(f"{cost_grid[y][x]}", True, (0, 0, 0))
            # _, _, text_w, text_h = text.get_rect()
            # text_x = ((box_pos[0] + box_size[0] / 2) - text_w / 2)
            # text_y = ((box_pos[1] + box_size[1] / 2) - text_h / 2)
            # text_pos = (text_x, text_y)
            # screen.blit(text, text_pos)
            if cost_grid[x][y] == 0:
                pg.draw.rect(screen, (0,177,0), (box_pos, box_size))
            elif cost_grid[x][y] == 1:
                pg.draw.rect(screen, (4,99,4), (box_pos, box_size))
            else:
                pg.draw.rect(screen, (0, 100, 255), (box_pos, box_size))
            pg.draw.rect(screen, (0, 0, 0), (box_pos, box_size), 1)

def cost_grid(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    box_list = []
    for x in range(int(height / box_size[0])):
        box_list.append([])
        for y in range(int(width / box_size[1])):
            nums = [0,1,5]
            box_list[x].append(random.choice(nums))

    return box_list

def node_grid(screen):
    width = screen.get_width()
    height = screen.get_height()
    box_size = (25, 25)
    node_list = []
    for x in range(0, width, box_size[0]):
        for y in range(0, height, box_size[1]):
            node_list.append([x, y])

    return node_list

def neighbors(node_list):
    #[1, 1], [-1, -1], [1, -1], [-1, 1]
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for node in node_list:
        for di in dirs:
            neighbor = [node[0] + di[0] * 25, node[1] + di[1] * 25]
            if neighbor[0] < 0 or neighbor[1] < 0:
                neighbor[0], neighbor[1] = 0, 0
            result.append(neighbor)
    return result
def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    grid = cost_grid(screen)
    draw_tiles(screen, grid)
    #print(grid)
    player_pos, goal_pos = draw_champ_n_goal(screen, grid)

    nodes = node_grid(screen)
    result = neighbors(nodes)
    print(result)
    print(player_pos, goal_pos)
    if player_pos in result:
        print("HELL YEAH")




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

