#!/usr/bin/env python3
import copy

import tcod

from input_handlers import EventHandler
import entity_factories
from engine import Engine
#from game_map import GameMap
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    #player_x = int(screen_width / 2)
    #player_y = int(screen_height / 2)

    

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)
    

    #engine = Engine(entities, event_handler, player)

    #game_map = GameMap(map_width, map_height)
    #game_map = generate_dungeon(map_width, map_height)
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )

    engine = Engine(event_handler = event_handler, game_map = game_map, player = player)



    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Dungeon Crawler",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:

            engine.render(root_console, context)

            events = tcod.event.wait()

            engine.handle_events(events)
            
            """
            #root_console.print(x=player_x, y=player_y, string="@")
            root_console.print(x = player.x, y = player.y, string = player.char, fg = player.color)

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    #player_x += action.dx
                    #player_y += action.dy

                    player.move(dx = action.dx, dy = action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()
                """


if __name__ == "__main__":
    main()