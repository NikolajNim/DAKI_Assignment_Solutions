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
    image_path = r"C:\Users\Nikolaj Nim\OneDrive - Aalborg Universitet\Dokumenter\GitHub\DAKI_Assignment_Solutions\KingDomino\KingDominoTestData\65.jpg"
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

    # Prompter useren omkring hvor mange tiles modellen fik rigtig
    correct_tiles = int(input("Enter the number of correct tiles: "))

    # Udregner nøjagtighed
    total_tiles = field + forest + lake + grassland + swamp + mine + home + unknown
    accuracy = (correct_tiles / total_tiles) * 100
    print(f"Accuracy: {accuracy:.2f}%")


# Tæller antallet af unikt terrain
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


# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y * 100 : (y + 1) * 100, x * 100 : (x + 1) * 100])
    return tiles


# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.mean(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    if 22 < hue < 34 and 209 < saturation < 260 and 119 < value < 201:
        return "Field"
    if 29 < hue < 63 and 85 < saturation < 201 and 36 < value < 84:
        return "Forest"
    if 74 < hue < 110 and 192 < saturation < 260 and 105 < value < 192:
        return "Lake"
    if 31 < hue < 50 and 161 < saturation < 237 and 73 < value < 162:
        return "Grassland"
    if 19 < hue < 39 and 57 < saturation < 170 and 52 < value < 134:
        return "Swamp"
    if 25 < hue < 54 and 57 < saturation < 140 and 43 < value < 91:
        return "Mine"
    if 17 < hue < 74 and 40 < saturation < 166 and 37 < value < 149:
        return "Home"
    return "Unknown"


if __name__ == "__main__":
    main()