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

        self.last_update_pos = None
        self.vertical_chunks = []
        self.horizontal_chunks = []

        self.world_map = self.create_world_map()

    @property
    def loaded_chunks(self):
        chunk_x, chunk_y = self.get_chunk_cords()

        chunks = []
        for y_offset in range(-self.engine.LOAD_DISTANCE, self.engine.LOAD_DISTANCE + 1):
            for x_offset in range(-self.engine.LOAD_DISTANCE, self.engine.LOAD_DISTANCE + 1):
                x = (chunk_x + x_offset) % self.world.chunks_size
                y = (chunk_y + y_offset) % self.world.chunks_size
                chunks.append((x, y))

        return chunks

    def get_chunk_cords(self):
        return (self.character.global_position.x // self.world.chunk_width,
                self.character.global_position.y // self.world.chunk_height)

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

        for index in range(len(self.loaded_chunks)):
            print(self.loaded_chunks[index], end=" ")
            if (index + 1) % 5 == 0:
                print()

        self.last_update_pos = self.get_chunk_cords()

        self.save_map(world_map, world_size=self.engine.INITIAL_WORLD_SIZE)
        return self.load_map()

    def update_chunks_cords(self):
        self.vertical_chunks.clear()
        self.horizontal_chunks.clear()

        chunk_x, chunk_y = self.get_chunk_cords()

        x_shift = (chunk_x - self.last_update_pos[0])
        y_shift = (chunk_y - self.last_update_pos[1])

        x_shift = x_shift if abs(x_shift) in (0, 1) else -(x_shift // abs(x_shift))
        y_shift = y_shift if abs(y_shift) in (0, 1) else -(y_shift // abs(y_shift))

        for x_offset in range(-self.engine.LOAD_DISTANCE * abs(x_shift),
                             (self.engine.LOAD_DISTANCE + 1) * abs(x_shift)):
            x = (chunk_x + self.engine.LOAD_DISTANCE * x_shift) % self.world.chunks_size
            y = (chunk_y + x_offset) % self.world.chunks_size
            self.vertical_chunks.append((x, y))

        for y_offset in range(-self.engine.LOAD_DISTANCE * abs(y_shift),
                             (self.engine.LOAD_DISTANCE + 1) * abs(y_shift)):
            x = (chunk_x + y_offset) % self.world.chunks_size
            y = (chunk_y + self.engine.LOAD_DISTANCE * y_shift) % self.world.chunks_size
            self.horizontal_chunks.append((x, y))

    def generate_chunks(self):

        with shelve.open("world_map", writeback=True) as db:

            new_chunks = self.horizontal_chunks + self.vertical_chunks

            for index in range(len(new_chunks)):
                chunk_cords = new_chunks[index]
                if db.get(f"chunk{chunk_cords[0]}_{chunk_cords[1]}") is None:
                    db[f"chunk{chunk_cords[0]}_{chunk_cords[1]}"] = self.world.map_generator.generate_by_chunk(chunk_cords[0], chunk_cords[1])

    # @functools.lru_cache(maxsize=4)
    def load_map(self):
        area = [[None for _ in range(self.engine.RENDERING_DISTANCE)] for _ in range(self.engine.RENDERING_DISTANCE)]
        with shelve.open("world_map", writeback=False, flag='r') as db:

            for index in range(len(self.loaded_chunks)):
                chunk_cord = self.loaded_chunks[index]
                x_ = index % self.engine.RENDERING_DISTANCE
                y_ = self.engine.RENDERING_DISTANCE - ceil((len(self.loaded_chunks) - index) / self.engine.RENDERING_DISTANCE)

                area[x_][y_] = db[f"chunk{chunk_cord[0]}_{chunk_cord[1]}"]

        return np.block(area)

    def update_map(self, world_copy):
        chunk_x, chunk_y = self.get_chunk_cords()

        x_shift = (chunk_x - self.last_update_pos[0])
        y_shift = (chunk_y - self.last_update_pos[1])
        x_shift = x_shift if abs(x_shift) in (0, 1) else -(x_shift // abs(x_shift))
        y_shift = y_shift if abs(y_shift) in (0, 1) else -(y_shift // abs(y_shift))

        horizontal_area = []
        vertical_area = []

        with shelve.open("world_map", writeback=False, flag='r') as db:

            for index in range(self.engine.RENDERING_DISTANCE):

                if x_shift:
                    chunk_cord = self.vertical_chunks[index]
                    if not ((y_shift == -1 and index == 0) or
                            (y_shift == 1 and index == self.engine.RENDERING_DISTANCE - 1)):
                        vertical_area.append(db[f"chunk{chunk_cord[0]}_{chunk_cord[1]}"])
                if y_shift:
                    chunk_cord = self.horizontal_chunks[index]
                    horizontal_area.append(db[f"chunk{chunk_cord[0]}_{chunk_cord[1]}"])

        if y_shift == 1:
            world_copy = world_copy[:, 50:].copy()
        elif y_shift == -1:
            world_copy = world_copy[:, :-50].copy()

        if x_shift:
            vertical_area = np.concatenate(vertical_area, axis=1)
        if y_shift:
            horizontal_area = np.concatenate(horizontal_area, axis=0)

        # print(f"current chunk: x: {self.character.global_position.x // self.world.chunk_width} "
        #       f"y: {self.character.global_position.y // self.world.chunk_height}")

        self.last_update_pos = (chunk_x, chunk_y)

        if x_shift == 1:
            world_copy = np.concatenate((world_copy[100:, :], vertical_area), axis=0)
        elif x_shift == -1:
            world_copy = np.concatenate((vertical_area, world_copy[:-100, :]), axis=0)
        if y_shift == 1:
            world_copy = np.concatenate((world_copy, horizontal_area), axis=1)
        elif y_shift == -1:
            world_copy = np.concatenate((horizontal_area, world_copy), axis=1)

        return world_copy

    def load_chunks(self, world_copy):

        self.update_chunks_cords()

        self.generate_chunks()
        world_map = self.update_map(world_copy)

        local_position = self.get_local_position(self.character.global_position.x,
                                                 self.character.global_position.y)

        self.shared_world_queue.put((world_map, (local_position[0], local_position[1])))

    def save_map(self, world_map, world_size):
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

        return not (self.engine.VIEWPORT_WIDTH // 2 < self.character_position.x + x < x_boundary) or \
           not (self.engine.VIEWPORT_HEIGHT < self.character_position.y + y < y_boundary)

    def character_sight(self, console=None):
        for y in range(-(self.engine.VIEWPORT_HEIGHT // 2), self.engine.VIEWPORT_HEIGHT // 2 + 1):
            for x in range(-(self.engine.VIEWPORT_WIDTH // 2), self.engine.VIEWPORT_WIDTH // 2 + 1):
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
                    threading.Thread(
                        target=self.load_chunks,
                        args=(world_copy,),
                        daemon=True
                    ).start()

            if hasattr(self, "shared_world_queue") and not self.shared_world_queue.empty():
                self.world_map, local_position = self.shared_world_queue.get()
                self.character_position.set_position(local_position[0], local_position[1])

                self.world_loading_in_progress = False

            # self.check_boundaries(x, y)
