import heapq
import random
import pygame as pg


class Astar:
    # The Astar class contains all the necessary methods for the A* algorithm.
    def __init__(self, matrix, matrix_size, box_size):
        # These are the necessary parameters to initialize this class:
        # A Matrix (List of lists), A Matrix size(columns and rows) and a box size when drawing with pygame.
        self.matrix = matrix
        self.matrix_size = matrix_size
        self.box_size = box_size

    def cost(self, p):
        # This method defines the cost of a specific value in the matrix.
        # The cost refers to the movement cost of a tile on the map made from the matrix.
        cost = [1, 2, 5, 1000]
        return cost[self.matrix[p[0]][p[1]] - 1]

    def color_picker(self, num):
        # This method returns an RGB-Color Tuple depending on what number is the input.
        if num == 1:
            return (0, 177, 0)  # Green.
        elif num == 2:
            return (4, 99, 4)  # Darker green.
        elif num == 5:
            return (0, 100, 255)  # Blue.
        else:
            return (82, 68, 57)  # Muddy brown.

    def draw_grid(self, screen):
        # This method uses a nested loop to iterate over the given matrix
        # and draw different colored squares and black outlines.
        # The different colors are based of the random numbers in the matrix, and they are processed
        # through the cost() and color_picker() metodes.
        # The positions of the squares are based on the x, y indexes in the matrix scaled with the box_size variable.
        for x, col in enumerate(self.matrix):
            for y, row in enumerate(col):
                pg.draw.rect(screen, self.color_picker(self.cost((x, y))),
                             ((x * self.box_size[0], y * self.box_size[1]), self.box_size))
                pg.draw.rect(screen, (0, 0, 0),
                             ((x * self.box_size[0], y * self.box_size[1]), self.box_size), 1)

    def draw_a_b(self, screen):
        # This method draws the start point(a) and end point(b) and returns their respective matrix index positions.
        red = (255, 0, 0)
        orange = (255, 140, 0)

        # The position of a is based on a random number between 0 and 31(current matrix size - 1)
        ax = random.randint(0, self.matrix_size[0] - 1)
        ay = random.randint(0, self.matrix_size[1] - 1)
        a_pos = (ax * self.box_size[0], ay * self.box_size[1])
        a_matrix_pos = (ax, ay)

        # The position of b is based on the position of a.
        # By subtracting the matrix size with a, the opposite position is the result.
        # And this is the chosen position for b.
        bx = self.matrix_size[0] - ax
        by = self.matrix_size[1] - ay
        b_pos = (bx * self.box_size[0] - self.box_size[0], by * self.box_size[1] - self.box_size[1])
        b_matrix_pos = (bx - 1, by - 1)

        pg.draw.rect(screen, red, (a_pos, self.box_size))
        pg.draw.rect(screen, orange, (b_pos, self.box_size))

        return a_matrix_pos, b_matrix_pos

    def neighbors(self, node):
        # This metode returns a list of all neighbors to a specific point(node).
        # Add these to directions for diagonal movement: [1, 1], [-1, -1], [-1, 1], [1, -1]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []

        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            # Only add the neighbor to the list, if it exists within the matrix.
            if 0 <= neighbor[0] < len(self.matrix) and 0 <= neighbor[1] < len(self.matrix[0]):
                result.append(neighbor)
        return result

    def heuristic(self, a, b):
        # This method calculates the distance between two point(a and b).
        # It is used to help the A* algorithm prioritize what direction to choose.
        (ax, ay) = a
        (bx, by) = b
        return abs(ax - bx) + abs(ay - by)

    def astar_search(self, a, b):
        # This method searches for point b starting from point a.
        frontier = [(0, a)]
        came_from = {}
        cost_so_far = {}
        came_from[a] = None
        cost_so_far[a] = 0

        while frontier:
            # frontier is a list
            current_priority, current = heapq.heappop(frontier)

            if current == b:
                # Ends the method early when b is found.
                break

            for next_node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(next_node)
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(b, next_node)
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