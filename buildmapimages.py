from PIL import Image, ImageFilter
from pathlib import Path


def print_map(lair):
    # Builds the map.png for the overview of the dungeon
    im = Image.open('transparent.png')
    data_folder = Path("10pxFloor/")
    ch1 = Image.open(data_folder / 'map-crosshatch0.png')
    ch2 = Image.open(data_folder / 'map-crosshatch1.png')
    mapimage = im.resize((lair.MAP_WIDTH*10, lair.MAP_HEIGHT*10))
    for y in range(lair.MAP_HEIGHT):
        for x in range(lair.MAP_WIDTH):
            position = (x*10, y*10)
            if lair.map[y][x] > 0:
                if lair.map[y][x] > 0:
                    p1 = p2 = p3 = p4 = 0
                    if lair.map[y][x - 1] < 1:
                        p1 = 1
                    if lair.map[y][x + 1] < 1:
                        p3 = 1
                    if lair.map[y - 1][x] < 1:
                        p2 = 1
                    if lair.map[y + 1][x] < 1:
                        p4 = 1
                    fl = Image.open(data_folder / ("map-genericfloor-"+str(p1)+str(p2)+str(p3)+str(p4)+".png"))
                    mapimage.paste(fl, position)
                if int(lair.map[y][x]) < 99:
                    num_position = ((x * 10) - 28, (y * 10) - 28)
                    data_folder = Path("40pxFloor/")
                    n1 = Image.open(data_folder / ("map-" + str(lair.map[y][x]) + ".png"))
                    mapimage.paste(n1, num_position)
                    data_folder = Path("10pxFloor/")
                elif int(lair.map[y][x]) == 100:
                    num_position = ((x * 10) + 1, (y * 10) + 1)
                    n1 = Image.open(data_folder / ("map-" + str(lair.map[y][x]) + ".png"))
                    mapimage.paste(n1, num_position)
                if lair.map[y][x] == 1:
                    mapimage.paste(n1, position)

            else:
                if lair.map[y][x] == 0:
                    mapimage.paste(ch1, position)
                else:
                    mapimage.paste(ch2, position)
    mapimage.save('map.png')
