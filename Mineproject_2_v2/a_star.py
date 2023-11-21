import heapq
import random
from queue import PriorityQueue
import pygame as pg
class Astar:
    def __init__(self, matrix, matrix_size, box_size):
        self.matrix = matrix
        self.matrix_size = matrix_size
        self.box_size = box_size


    def color_picker(self, rand_num):
        if rand_num == 1:
            return (0, 177, 0)
        elif rand_num == 2:
            return (4, 99, 4)
        elif rand_num == 5:
            return (0, 100, 255)
        else:
            return (20, 20, 20)

    def cost(self, point):
        cost = [1, 2, 5, 1000]
        return cost[self.matrix[point[0]][point[1]] - 1]
    def draw_grid(self, screen):

        for x, col in enumerate(self.matrix):
            for y, row in enumerate(col):
                pg.draw.rect(screen, self.color_picker(self.cost((x, y))), ((x * self.box_size[0], y * self.box_size[1]), self.box_size))
                pg.draw.rect(screen, (0, 0, 0), ((x * self.box_size[0], y * self.box_size[1]), self.box_size), 1)

    def draw_a_b(self, screen):
        red = (255, 0, 0)
        orange = (255, 140, 0)

        ax = random.randint(0, self.matrix_size[0] - 1)
        ay = random.randint(0, self.matrix_size[1] - 1)
        a_pos = (ax * self.box_size[0], ay * self.box_size[1])
        a_matrix_pos = (ax, ay)

        bx = self.matrix_size[0] - ax
        by = self.matrix_size[1] - ay
        b_pos = (bx * self.box_size[0] - self.box_size[0], by * self.box_size[1] - self.box_size[1])
        b_matrix_pos = (bx - 1, by - 1)

        pg.draw.rect(screen, red, (a_pos, self.box_size))
        pg.draw.rect(screen, orange, (b_pos, self.box_size))

        return a_matrix_pos, b_matrix_pos


    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []

        for dir in dirs:
            neighbor = (node[0] + dir[0], node[1] + dir[1])
            if 0 <= neighbor[0] < len(self.matrix) and 0 <= neighbor[1] < len(self.matrix[0]):
                result.append(neighbor)
        return result
    def heuristic(self, a, b):
        (ax, ay) = a
        (bx, by) = b

        return abs(ax - bx) + abs(ay - by)

    def astar_search(self, a, b):
        frontier = [(0, a)]
        came_from = {}
        cost_so_far = {}
        came_from[a] = None
        cost_so_far[a] = 0

        while frontier:
            current_priority, current = heapq.heappop(frontier)
            print(f"Current in astar_search: {current}")
            #print(f"a in astar_search: {a}")
            #print(f"b in astar_search: {b}")
            #print(f"current in astar_search: {current}")
            if current == b:
                print("Halløj")
                break

            for next_node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(next_node)
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(b, next_node)
                    #print(f"priority from astar_search: {priority}")
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current

        return came_from, cost_so_far

    def reconstruct(self, came_from, a, b):
        current = b
        path = []
        if b not in came_from:
            return []
        while current != a:
            path.append(current)
            current = came_from[current]
        path.append(a)
        path.reverse()
        return path