import shelve
import functools

import numpy as np


class Map:

    def __init__(self,
                 world,
                 width=30,
                 height=30,
                 ):
        self.world = world
        self.engine = self.world.engine
        self.width = width
        self.height = height

        self.character = self.world.character
        self.character_position = self.character.position

        self.world_map = None
        self.create_world_map()

    # TODO: Make function that sets load position in chunk local coordinate system not in global cords system.
    def get_local_position(self, x, y):
        return self.engine.LOAD_DISTANCE * self.world.chunk_width + x % self.world.chunk_width, \
               self.engine.LOAD_DISTANCE * self.world.chunk_height + y % self.world.chunk_height

    def create_world_map(self):
        start_position = self.world.map_generator.get_location(0.4, 1)
        world_map = self.world.map_generator.generate_initial_map(
            start_x=start_position[0],
            start_y=start_position[1],
            width=self.engine.INITIAL_WORLD_SIZE, height=self.engine.INITIAL_WORLD_SIZE
        )

        load_position = self.get_local_position(start_position[0], start_position[1])
        self.character.global_position.set_position(start_position[0], start_position[1])
        self.character_position.set_position(load_position[0], load_position[1])

        self.save_map(world_map, world_size=self.engine.INITIAL_WORLD_SIZE)
        self.world_map = self.load_map()

    def generate_chunks(self, direction_x: int, direction_y: int):
        # x = (self.character_position.x // self.world.chunk_width + (direction_x * (self.engine.LOAD_DISTANCE + 1))
        #      ) % (self.world.width // self.world.chunk_width)
        # y = (self.character_position.y // self.world.chunk_height + (direction_y * (self.engine.LOAD_DISTANCE + 1))
        #      ) % (self.world.height // self.world.chunk_height)
        x = (self.character.global_position.x // self.world.chunk_width +
             (direction_x * (self.engine.LOAD_DISTANCE + 1))) % (self.world.width // self.world.chunk_width)
        y = (self.character.global_position.y // self.world.chunk_height +
             (direction_y * (self.engine.LOAD_DISTANCE + 1))) % (self.world.height // self.world.chunk_height)

        with shelve.open("world_map", writeback=True) as db:
            for chunk_y in range(y - (self.engine.LOAD_DISTANCE * abs(direction_x)),
                                 y + (self.engine.LOAD_DISTANCE + 1) * abs(direction_x)):
                for chunk_x in range(x - (self.engine.LOAD_DISTANCE * abs(direction_y)),
                                     x + ((self.engine.LOAD_DISTANCE + 1) * abs(direction_y))):
                    if not db.get(f"chunk{chunk_x}_{chunk_y}"):
                        db[f"chunk{chunk_x}_{chunk_y}"] = self.world.map_generator.generate_by_chunk(chunk_x, chunk_y)
        print("generate check")

    # @functools.lru_cache(maxsize=4)
    def load_map(self):
        range_: np.ndarray = [
            [(x, y) for x in range(-self.engine.LOAD_DISTANCE, self.engine.LOAD_DISTANCE + 1)]
            for y in range(-self.engine.LOAD_DISTANCE, self.engine.LOAD_DISTANCE + 1)
        ]
        area: np.ndarray = None
        with shelve.open("world_map", writeback=False) as db:

            chunk_x = self.character.global_position.x // self.world.chunk_width
            chunk_y = self.character.global_position.y // self.world.chunk_height

            for y in range(chunk_y - self.engine.LOAD_DISTANCE, chunk_y + self.engine.LOAD_DISTANCE + 1):
                for x in range(chunk_x - self.engine.LOAD_DISTANCE, chunk_x + self.engine.LOAD_DISTANCE + 1):
                    print(x, y)
                    if area is None:
                        area = db[f"chunk{x}_{y}"]
                        continue
                    area = np.concatenate((area, db[f"chunk{x}_{y}"]), axis=0)

            # for y in range(self.engine.RENDERING_DISTANCE):
            #     for x in range(self.engine.RENDERING_DISTANCE):
            #         offset = range_[y][x]
            #         # x_ = self.character_position.x // self.world.chunk_width + offset[0]
            #         # y_ = self.character_position.y // self.world.chunk_height + offset[1]
            #         chunk_x = self.character.global_position.x // self.world.chunk_width + offset[0]
            #         chunk_y = self.character.global_position.y // self.world.chunk_height + offset[1]
            #         if area is None:
            #             area = db[f"chunk{chunk_x}_{chunk_y}"]
            #             continue
            #         area = np.concatenate((area, db[f"chunk{chunk_x}_{chunk_y}"]), axis=0)

        new_position = self.get_local_position(self.character.global_position.x,
                                               self.character.global_position.y)
        print(new_position)
        self.character_position.set_position(new_position[0], new_position[1])

        print("load check")
        print(area.shape)

        return area.reshape((self.engine.RENDERING_DISTANCE * self.world.chunk_width,
                             self.engine.RENDERING_DISTANCE * self.world.chunk_height))

    def save_map(self, world_map, world_size=None):
        if not world_size:
            world_size = self.engine.RENDERING_DISTANCE
        # chunk_x = self.character_position.x // self.world.chunk_width
        # chunk_y = self.character_position.y // self.world.chunk_height
        chunk_y = self.character.global_position.y // self.world.chunk_height
        chunk_x = self.character.global_position.x // self.world.chunk_width
        world_map = world_map.reshape((world_size, world_size,
                                       self.world.chunk_width, self.world.chunk_height))
        with shelve.open("world_map", writeback=True) as db:
            # can't think of anything better than this
            y_ = 0
            for y in range(chunk_y - self.engine.LOAD_DISTANCE, chunk_y + self.engine.LOAD_DISTANCE + 1):
                x_ = 0
                for x in range(chunk_x - self.engine.LOAD_DISTANCE, chunk_x + self.engine.LOAD_DISTANCE + 1):
                    # db[f"chunk{x}_{y}"] = world_map[y % world_map.shape[1]][x % world_map.shape[0]]
                    db[f"chunk{x}_{y}"] = world_map[y_][x_]
                    x_ += 1
                y_ += 1
        print("save check")

    def check_boundaries(self, x, y):
        x_boundary = (self.engine.RENDERING_DISTANCE * self.world.chunk_width) - (self.engine.VIEWPORT_WIDTH // 2)
        y_boundary = self.engine.RENDERING_DISTANCE * self.world.chunk_height - self.engine.VIEWPORT_HEIGHT

        if not (self.engine.VIEWPORT_WIDTH // 2 < self.character_position.x + x < x_boundary) or \
           not (self.engine.VIEWPORT_HEIGHT < self.character_position.y + y < y_boundary):

            self.save_map(self.world_map)
            self.generate_chunks(x, y)
            self.world_map = self.load_map()
            print("check_boundary")

    def character_sight(self, console=None):
        for y in range(-(self.engine.VIEWPORT_HEIGHT // 2), self.engine.VIEWPORT_HEIGHT // 2 + 1):
            for x in range(-(self.engine.VIEWPORT_WIDTH // 2), self.engine.VIEWPORT_WIDTH // 2 + 1):
                tile = self.world_map[
                    (x + self.character_position.x) % (self.engine.RENDERING_DISTANCE * self.world.chunk_width)][
                    (y + self.character_position.y) % (self.engine.RENDERING_DISTANCE * self.world.chunk_height)]

                console.print(x + self.engine.VIEWPORT_WIDTH // 2, y + self.engine.VIEWPORT_HEIGHT // 2, " ",
                              bg=tile.biome.bg_color)
        console.print(self.engine.VIEWPORT_WIDTH // 2, self.engine.VIEWPORT_HEIGHT // 2, "@", fg=(0, 0, 0))

    def check_passability(self, x, y):
        # return not (self.world_map[x, y].biome.passability > 0)
        return True

    def move(self, x, y):
        # _x = (self.character_position.x + x) % self.width
        # _y = (self.character_position.y + y) % self.height

        local_x = (self.character_position.x + x) % (self.world.chunk_width * self.engine.RENDERING_DISTANCE)
        local_y = (self.character_position.y + y) % (self.world.chunk_height * self.engine.RENDERING_DISTANCE)
        global_x = (self.character.global_position.x + x) % self.width
        global_y = (self.character.global_position.y + y) % self.height

        if self.check_passability(local_x, local_y):
            # if self.check_passability(_x, _y):
            # self.character_position.set_position(_x, _y)

            self.character_position.set_position(local_x, local_y)
            self.character.global_position.set_position(global_x, global_y)
            self.check_boundaries(x, y)

            print("Local position: ", self.world.character.position)
            print("Global position: ", self.character.global_position)
            print("Chunk x: ", self.character.global_position.x // self.world.chunk_width)
            print("Chunk y: ", self.character.global_position.y // self.world.chunk_height)
            # print(self.load_position)
