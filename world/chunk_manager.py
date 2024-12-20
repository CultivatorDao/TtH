import math

from .zones.chunk import Chunk


class ChunkManager:

    def __init__(self, world):
        self.world = world

        self.world_width = self.world.size[0]
        self.world_height = self.world.size[1]
        self.chunk_size = self.world.chunk_size

        self.chunks = []
        self.generate_chunks()

    @property
    def max_chunk_position(self):
        """
        Returns tuple in which first number is max y position and second number is max x position.
        :return: tuple[int, int]
        """
        return math.ceil(self.world_width / self.chunk_size) - 1, math.ceil(self.world_height / self.chunk_size) - 1

    def generate_chunks(self):
        y_max, x_max = self.max_chunk_position
        for y_range in range(y_max + 1):
            row = []
            for x_range in range(x_max + 1):
                x = self.chunk_size * x_range
                y = self.chunk_size * y_range
                row.append(Chunk(
                    manager=self,
                    x=x,
                    y=y,
                ))
            self.chunks.append(row)

    def current_chunk_position(self, x, y):
        # If we divide world width or height by chunk size we will get amount of chunks in row/column.
        # If we divide current coordinates by chunk size we'll get chunk index + 1.
        # So if we subtract 1 we'll get its index.
        # First chunk coordinates starts from 0 and ends to chunk size - 1.
        return (x // self.chunk_size - (x == self.world_width)), (y // self.chunk_size - (y == self.world_height))

    def current_chunk(self, x, y):
        _x, _y = self.current_chunk_position(x, y)
        return self.chunks[_y][_x]

    def nearest_chunks(self, x, y):
        current_position = self.current_chunk_position(x, y)
        chunks = []
        # Get vectors(directions) to coordinates around given x, y.
        for _y in range(-1, 2):
            for _x in range(-1, 2):
                # Position cannot be negative and bigger than max chunks amount.
                if 0 <= current_position[0] + _x <= self.max_chunk_position[1] \
                        and 0 <= current_position[1] + _y <= self.max_chunk_position[0]:
                    # print(self.chunks)
                    # print(current_position[1] - _y, current_position[0] - _x)
                    chunks.append(self.chunks[current_position[1] + _y][current_position[0] + _x])
        return chunks
