import pygame as pg
import random
from queue import PriorityQueue
class AStar:

    def __init__(self):
        pass

    def heuristic(self, point_a, point_b):
        [x1, y1] = point_a
        [x2, y2] = point_b

        return  abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(self, graph, start , goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from: dict[start] = {}
        cost_so_far: dict[start, float] = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current: start = frontier.get()

            if current == goal:
                break




    def draw_champ_n_goal(self, screen, cost_grid, box_size=(25, 25)):
        red = (255, 0, 0)
        magenta = (255, 0, 255)
        width = screen.get_width()
        height = screen.get_height()
        rand_pos_x = random.randrange(len(cost_grid))
        rand_pos_y = random.randrange(len(cost_grid))

        player_box_pos = [rand_pos_x * box_size[0], rand_pos_y * box_size[1]]
        pg.draw.rect(screen, red, (player_box_pos, box_size))

        goal_x = width - rand_pos_x * box_size[0] - box_size[0]
        goal_y = height - rand_pos_y * box_size[1] - box_size[1]
        goal_box_pos = [goal_x, goal_y]
        pg.draw.rect(screen, magenta, (goal_box_pos, box_size))

        return player_box_pos, goal_box_pos