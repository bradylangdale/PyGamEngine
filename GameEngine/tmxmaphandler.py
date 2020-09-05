import importlib
from pytmx.util_pygame import load_pygame


def load_map(path):  # loads  tmx tile map
    tiled_map = load_pygame(path)
    game_objects = []

    for layer in tiled_map.layers:  # iterates through all layers of the tile map
        class_name = layer.properties['class_name']
        class_name = getattr(importlib.import_module(class_name.lower()), class_name)
        for x, y, image in layer.tiles():  # iterates through tiles in layer
            # creates an instance of class_name with the attributes of the layer
            game_object = class_name(x*tiled_map.tilewidth, y*tiled_map.tileheight, image)
            game_object.density = layer.properties['density']
            game_object.dynamic = True if layer.properties['dynamic'] == 1 else False
            game_object.rotates = True if layer.properties['rotates'] == 0 else False
            game_objects.append(game_object)
            # generates game objects
    return game_objects
