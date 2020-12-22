from typing import Tuple
import numpy as np

# Tile graphics structured type copatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # Unicode codepoint
        ("fg", "3B"), # 3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphic_dt),
    ]
)


def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype = tile_dt)

floor = new_tile(
    walkable = True, transparent = True, dark = (ord(" "), (255, 255, 255), (50, 50, 150)),
)

wall = new_tile(
    walkable = False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100)),
)