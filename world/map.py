import shelve
import threading
import queue
from math import ceil

import numpy as np

from world.biomes.biome import EmptyBiome
from world.map_tile import MapTile


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

        self.db_lock = threading.Lock()

        self.shared_world_queue = queue.Queue()
        self.world_loading_in_progress = False

        self.last_save_pos = None
        self.loaded_chunks = []

        self.world_map = None
        self.create_world_map()
        # self.world_map = self.load_map()

        # self.character.set_position(200, 153)
        # self.character.global_position.set_position(200, 153)
        # self.world_map = self.load_map()

    def get_local_position(self, x, y):
        return self.engine.LOAD_DISTANCE * self.world.chunk_width + x % self.world.chunk_width, \
               self.engine.LOAD_DISTANCE * self.world.chunk_height + y % self.world.chunk_height
        # return self.engine.LOAD_DISTANCE * self.world.chunk_width, \
        #        self.engine.LOAD_DISTANCE * self.world.chunk_height

    def create_world_map(self):
        start_position = self.world.map_generator.get_location(0.5, 1)
        world_map = self.world.map_generator.generate_initial_map(
            start_x=start_position[0],
            start_y=start_position[1],
            width=self.engine.INITIAL_WORLD_SIZE, height=self.engine.INITIAL_WORLD_SIZE
        )

        load_position = self.get_local_position(start_position[0], start_position[1])
        print(f"load_position: {load_position}")
        self.character.global_position.set_position(start_position[0], start_position[1])
        self.character_position.set_position(load_position[0], load_position[1])
        print(f"global start pos: {self.character.global_position}")
        print(f"local start pos: {self.character_position}")

        self.load_chunks_cords()
        self.save_map(world_map, world_size=self.engine.INITIAL_WORLD_SIZE)
        self.world_map = self.load_map()

    def load_chunks_cords(self):
        self.loaded_chunks.clear()

        chunk_x = self.character.global_position.x // self.world.chunk_width
        chunk_y = self.character.global_position.y // self.world.chunk_height
        # print(f"current chunk: x: {chunk_x} y: {chunk_y}")

        for y_offset in range(-self.engine.LOAD_DISTANCE, self.engine.LOAD_DISTANCE + 1):
            for x_offset in range(-self.engine.LOAD_DISTANCE, self.engine.LOAD_DISTANCE + 1):
                x = (chunk_x + x_offset) % self.world.chunks_size
                y = (chunk_y + y_offset) % self.world.chunks_size
                self.loaded_chunks.append((x, y))


    def generate_chunks(self):

        # print("Local position: ", self.world.character.position)
        # print("Global position: ", self.character.global_position)
        # print("Chunk x: ", self.character.global_position.x // self.world.chunk_width)
        # print("Chunk y: ", self.character.global_position.y // self.world.chunk_height)

        with shelve.open("world_map", writeback=True) as db:

            for index in range(len(self.loaded_chunks)):
                chunk_cords = self.loaded_chunks[index]
                if db.get(f"chunk{chunk_cords[0]}_{chunk_cords[1]}") is None:
                    db[f"chunk{chunk_cords[0]}_{chunk_cords[1]}"] = self.world.map_generator.generate_by_chunk(chunk_cords[0], chunk_cords[1])


    # @functools.lru_cache(maxsize=4)
    def load_map(self):
        area = [[None for _ in range(self.engine.RENDERING_DISTANCE)] for _ in range(self.engine.RENDERING_DISTANCE)]
        with shelve.open("world_map", writeback=False) as db:

            for index in range(len(self.loaded_chunks)):
                chunk_cord = self.loaded_chunks[index]
                x_ = index % self.engine.RENDERING_DISTANCE
                y_ = self.engine.RENDERING_DISTANCE - ceil((len(self.loaded_chunks) - index) / self.engine.RENDERING_DISTANCE)

                area[x_][y_] = db[f"chunk{chunk_cord[0]}_{chunk_cord[1]}"]

        # new_position = self.get_local_position(self.character.global_position.x,
        #                                        self.character.global_position.y)
        # print(f"new_pos: {new_position}")
        # self.character_position.set_position(new_position[0], new_position[1])

        # return area.reshape((self.engine.RENDERING_DISTANCE * self.world.chunk_width,
        #                      self.engine.RENDERING_DISTANCE * self.world.chunk_height))
        return np.block(area)

    def load_chunks(self, world_copy):
        self.save_map(world_copy, self.engine.RENDERING_DISTANCE)
        self.load_chunks_cords()
        self.generate_chunks()
        world_map = self.load_map()

        local_position = self.get_local_position(self.character.global_position.x,
                                                 self.character.global_position.y)

        self.shared_world_queue.put((world_map, (local_position[0], local_position[1])))

    def save_map(self, world_map, world_size):

        # test_se = world_map[100:200, 50:100]
        #
        # for test_y_ in range(0, 50):
        #     for test_x_ in range(0, 100):
        #         if test_se[test_x_][test_y_].biome.name == "Ocean":
        #             print("0", end="")
        #         else:
        #             print("1", end="")
        #     print()
        #
        # world_map = world_map.reshape((world_size, world_size,
        #                                self.world.chunk_width, self.world.chunk_height))
        #
        # for test_y in range(50):
        #     for test_x in range(100):
        #         if world_map[1][1][test_x][test_y].biome.name == "Ocean":
        #             print("0", end="")
        #         else:
        #             print("1", end="")
        #     print()

        with shelve.open("world_map", writeback=True) as db:
            for index in range(len(self.loaded_chunks)):
                chunk_cord = self.loaded_chunks[index]
                x_ = index % self.engine.RENDERING_DISTANCE
                y_ = self.engine.RENDERING_DISTANCE - ceil((len(self.loaded_chunks) - index) / self.engine.RENDERING_DISTANCE)
                db[f"chunk{chunk_cord[0]}_{chunk_cord[1]}"] = world_map[
                    x_ * self.world.chunk_width:(x_ + 1) * self.world.chunk_width,
                    y_ * self.world.chunk_height: (y_ + 1) * self.world.chunk_height]


    def check_boundaries(self, x, y):
        x_boundary = (self.engine.RENDERING_DISTANCE * self.world.chunk_width) - (self.engine.VIEWPORT_WIDTH // 2)
        y_boundary = self.engine.RENDERING_DISTANCE * self.world.chunk_height - self.engine.VIEWPORT_HEIGHT

        # if not (self.engine.VIEWPORT_WIDTH // 2 < self.character_position.x + x < x_boundary) or \
        #    not (self.engine.VIEWPORT_HEIGHT < self.character_position.y + y < y_boundary):
        return not (self.engine.VIEWPORT_WIDTH // 2 < self.character_position.x + x < x_boundary) or \
           not (self.engine.VIEWPORT_HEIGHT < self.character_position.y + y < y_boundary)
            # print(f"pre char + coord:  x: {self.character_position.x + x} y: {self.character_position.y + y}")
            # print(f"x_boundary: {x_boundary} | y_boundary: {y_boundary}")

            # self.save_map(world_copy, self.engine.RENDERING_DISTANCE)
            # self.load_chunks_cords()
            # self.generate_chunks()
            # world_map = self.load_map()
            #
            # local_position = self.get_local_position(self.character.global_position.x,
            #                                          self.character.global_position.y)
            #
            # self.shared_world_queue.put((world_map, (local_position[0], local_position[1])))

    def character_sight(self, console=None):
        for y in range(-(self.engine.VIEWPORT_HEIGHT // 2), self.engine.VIEWPORT_HEIGHT // 2 + 1):
            for x in range(-(self.engine.VIEWPORT_WIDTH // 2), self.engine.VIEWPORT_WIDTH // 2 + 1):
                # finally (i hope) find where is the problem with rendering
                # should've used global position for rendering
                # but there is new problem
                # chunks are not generating as expecting
                # tile = self.world_map[
                #     (x + self.character.global_position.x) % (self.engine.RENDERING_DISTANCE * self.world.chunk_width)][
                #     (y + self.character.global_position.y) % (self.engine.RENDERING_DISTANCE * self.world.chunk_height)]
                tile_x = x + self.character.position.x
                tile_y = y + self.character.position.y
                map_size = self.world_map.shape
                if tile_x >= map_size[0] or tile_y >= map_size[1]:
                    tile = MapTile(EmptyBiome())
                else:
                    tile = self.world_map[tile_x][tile_y]

                console.print(x + self.engine.VIEWPORT_WIDTH // 2, y + self.engine.VIEWPORT_HEIGHT // 2, " ",
                              bg=tile.biome.bg_color)
        console.print(self.engine.VIEWPORT_WIDTH // 2, self.engine.VIEWPORT_HEIGHT // 2, "@", fg=(0, 0, 0))
        console.print(0, self.engine.VIEWPORT_HEIGHT + 1, f"x: {self.character.global_position.x}")
        console.print(10, self.engine.VIEWPORT_HEIGHT + 1, f"y: {self.character.global_position.y}")
        console.print(40, self.engine.VIEWPORT_HEIGHT + 1, f"local x: {self.character.position.x}")
        console.print(60, self.engine.VIEWPORT_HEIGHT + 1, f"local y: {self.character.position.y}")
        console.print(0, self.engine.VIEWPORT_HEIGHT + 2, f"x_chunk: {self.character.global_position.x // self.world.chunk_width}")
        console.print(15, self.engine.VIEWPORT_HEIGHT + 2, f"y_chunk: {self.character.global_position.y // self.world.chunk_height}")

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

            if self.check_boundaries(x, y):
                if not getattr(self, "world_loading_in_progress", False):
                    self.world_loading_in_progress = True

                    world_copy = self.world_map.copy()
                    print(world_copy.shape)
                    threading.Thread(
                        target=self.load_chunks,
                        args=(world_copy,),
                        daemon=True
                    ).start()
                    print("check ")

            if hasattr(self, "shared_world_queue") and not self.shared_world_queue.empty():
                print("check load")
                self.world_map, local_position = self.shared_world_queue.get()
                self.character_position.set_position(local_position[0], local_position[1])

                self.world_loading_in_progress = False

            # self.check_boundaries(x, y)

            # print("Local position: ", self.world.character.position)
            # print("Global position: ", self.character.global_position)
            # print("Chunk x: ", self.character.global_position.x // self.world.chunk_width)
            # print("Chunk y: ", self.character.global_position.y // self.world.chunk_height)
            # print(self.load_position)
