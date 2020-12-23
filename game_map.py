import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        #self.tiles = np.full((width, height), fill_value = tile_types.floor, order = "F")
        self.tiles = np.full((width, height), fill_value = tile_types.wall, order = "F")
        #self.tiles[30:33, 22] = tile_types.wall

        self.visible = np.full((width, height), fill_value = False, order = "F") # Tiles the player could currently see
        self.explored = np.full((width, height), fill_value = False, order = "F") # Tiles the player visisted previously

    def in_bound(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        
        """
        Renders the map.

        If a tile is in the "visible" array, we draw it with light color
        If it isn't, but it is in "explored" colors, we draw it with dark color
        Otherwise, the default is SHROUD
        """
        
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist = [self.visible, self.explored],
            choicelist = [self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUND
        )