from __future__ import annotations

from typing import Iterable, TYPE_CHECKING

import numpy as np
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity

class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        #self.tiles = np.full((width, height), fill_value = tile_types.floor, order = "F")
        self.entities = set(entities)
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

        for entity in self.entities:
            
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg = entity.color)