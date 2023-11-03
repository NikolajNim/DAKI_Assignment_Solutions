from typing import Tuple, TypeVar

import pygame as pg
import random
from queue import PriorityQueue
Location = TypeVar("Location")
class AStar:

    def __init__(self, grid):
        self.grid = grid

    def heuristic(self, point_a, point_b):
        [x1, y1] = point_a
        [x2, y2] = point_b

        return abs(x1 - x2) + abs(y1 - y2)

    def neighbors(self, current_node, node_list):
        # [1, 1], [-1, -1], [1, -1], [-1, 1]
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        node = current_node
        #print(f"Node_list: {node_list}")
        for di in dirs:
            neighbor = (node[0] + di[0] * 25, node[1] + di[1] * 25)
            #print(f"Neighbor: {neighbor}")
            #print(neighbor in node_list)
            if neighbor in node_list:
                result.append(neighbor)
        return result
    def a_star_search(self, cost, grid, start , goal):
        frontier = PriorityQueue()
        frontier.put(start)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        print(f"Grid: {grid}")
        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break
            for new in self.neighbors(current, grid):
                new_cost = cost_so_far[current] + cost[int(current[0]/25)][int(current[1]/25)]
                if new not in came_from or new_cost < cost_so_far[new]:
                    cost_so_far[new] = new_cost
                    priority = new_cost + self.heuristic(new, goal)
                    frontier.put(new, priority)
                    came_from[new] = current
        return came_from, cost_so_far


    def reconstruct(self, came_from: dict[Location, Location], start: Location, goal: Location):
        current = goal
        path: list[Location] = []
        if goal not in came_from:
            print("LMAO")
            return []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        # for point in path:
        #     new_point = (point[0]+12, point[1]+12)
        #     path.remove(point)
        #     path.append(new_point)
        return path



    def draw_champ_n_goal(self, screen, cost_grid, box_size=(25, 25)):
        red = (255, 0, 0)
        magenta = (255, 0, 255)
        width = screen.get_width()
        height = screen.get_height()
        rand_pos_x = random.randrange(len(cost_grid))
        rand_pos_y = random.randrange(len(cost_grid))

        player_box_pos = (rand_pos_x * box_size[0], rand_pos_y * box_size[1])
        pg.draw.rect(screen, red, (player_box_pos, box_size))
        p_box_pos = (player_box_pos[0] + box_size[0]/2, player_box_pos[1] + box_size[1]/2)

        goal_x = width - rand_pos_x * box_size[0] - box_size[0]
        goal_y = height - rand_pos_y * box_size[1] - box_size[1]
        goal_box_pos = (goal_x, goal_y)
        pg.draw.rect(screen, magenta, (goal_box_pos, box_size))
        g_box_pos = (goal_box_pos[0] + box_size[0]/2, goal_box_pos[1] + box_size[1]/2)

        return p_box_pos, g_box_pos