import numpy as np

from datapoint import Datapoint
import random
import pygame as pg
from kNN import KNN
def main():
    screen = initiate_pygame()

    datapoints_salmon = instantiate_salmon(screen, 100)

    datapoints_sea_bass = instantiate_sea_bass(screen, 100)

    new_datapoint = Datapoint(400, 300, label=None, color=(0, 255, 0))
    new_datapoint.draw(screen)

    knn = KNN()

    X_train = []
    y_train = []

    for datapoint in datapoints_salmon:
        X_train.append([datapoint.x, datapoint.y])
        y_train.append(datapoint.label)

    for datapoint in datapoints_sea_bass:
        X_train.append([datapoint.x, datapoint.y])
        y_train.append(datapoint.label)

    knn.fit(X_train, y_train)

    new_datapoint_feature = [new_datapoint.x, new_datapoint.y]
    predicted_class = knn.predict([new_datapoint_feature])

    print("Predicted class: ", predicted_class)

    game_loop()


def instantiate_salmon(screen, num_of_instances):
    datapoints_salmon = []
    red = (255, 0, 0)
    for i in range(num_of_instances):
        datapoints_salmon.append(Datapoint(random.gauss(200, 20), random.gauss(200, 20), label="salmon", color=red))
    for datapoint_salmon in datapoints_salmon:
        datapoint_salmon.draw(screen)
    return datapoints_salmon


def instantiate_sea_bass(screen, num_of_instances):
    datapoints_sea_bass = []
    blue = (0, 0, 255)
    for i in range(num_of_instances):
        datapoints_sea_bass.append(
            Datapoint(random.gauss(400, 20), random.gauss(400, 20), label="sea bass", color=blue))
    for datapoint_sea_bass in datapoints_sea_bass:
        datapoint_sea_bass.draw(screen)
    return datapoints_sea_bass


def game_loop():
    run_flag = True
    while run_flag is True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_flag = False
        pg.display.flip()


def initiate_pygame():
    pg.init()  # Initialize Pygame
    screen = pg.display.set_mode((800, 800))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    return screen

if __name__ == "__main__":
    main()