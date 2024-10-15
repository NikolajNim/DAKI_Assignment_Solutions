import cv2 as cv
import numpy as np
import os


# Main function containing the backbone of the program
def main():
    global field, forest, lake, grassland, swamp, mine, home, unknown
    field, forest, lake, grassland, swamp, mine, home, unknown = 0, 0, 0, 0, 0, 0, 0, 0
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"C:\Users\Nikolaj Nim\OneDrive - Aalborg Universitet\Dokumenter\GitHub\DAKI_Assignment_Solutions\KingDomino\KingDominoTestData\1.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
    print(len(tiles))
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            terrain = get_terrain(tile)
            print(terrain)
            print("=====")
            count_tiles(terrain)

    terrain_count = f"Terrain Count:\nFields: {field}\nForests: {forest}\nLakes: {lake}\nGrasslands: {grassland}\nSwamps: {swamp}\nMines: {mine}\nHome: {home}\nUnknowns: {unknown}"
    print(terrain_count)

    # Ask the user for the number of correct tiles
    correct_tiles = int(input("Enter the number of correct tiles: "))

    # Calculate and display accuracy
    total_tiles = field + forest + lake + grassland + swamp + mine + home + unknown
    accuracy = (correct_tiles / total_tiles) * 100
    print(f"Accuracy: {accuracy:.2f}%")


# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y * 100:(y + 1) * 100, x * 100:(x + 1) * 100])
    return tiles


def count_tiles(tile):
    global field, forest, lake, grassland, swamp, mine, home, unknown
    if tile == "Field":
        field += 1
    elif tile == "Forest":
        forest += 1
    elif tile == "Lake":
        lake += 1
    elif tile == "Grassland":
        grassland += 1
    elif tile == "Swamp":
        swamp += 1
    elif tile == "Mine":
        mine += 1
    elif tile == "Home":
        home += 1
    elif tile == "Unknown":
        unknown += 1


# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.mean(hsv_tile, axis=(0, 1))  # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    if 24 < hue < 32 and 135 < saturation < 253 and 143 < value < 201:

        return "Field"
    if 34 < hue < 53 and 100 < saturation < 201 and 39 < value < 80:

        return "Forest"
    if 74 < hue < 107 and 193 < saturation < 250 and 115 < value < 189:

        return "Lake"
    if 31 < hue < 47 and 173 < saturation < 227 and 101 < value < 158:

        return "Grassland"
    if 21 < hue < 39 and 78 < saturation < 170 and 52 < value < 134:

        return "Swamp"
    if 28 < hue < 47 and 92 < saturation < 140 and 50 < value < 75:

        return "Mine"
    if 23 < hue < 61 and 65 < saturation < 138 and 49 < value < 141:

        return "Home"
    return "Unknown"


if __name__ == "__main__":
    main()
