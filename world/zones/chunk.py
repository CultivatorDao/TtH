from components.geometry_component import GeometryComponent


class Chunk:

    def __init__(self, manager, x, y):
        self.manager = manager

        self.size = self.manager.chunk_size

        self.x_start = x
        self.y_start = y
        self.x_end = min(self.x_start + self.size - 1, self.manager.world_width)
        self.y_end = min(self.y_start + self.size - 1, self.manager.world_height)

        self.geometry = GeometryComponent(x=x,
                                          y=y,
                                          width=self.size,
                                          height=self.size)

        self.zones = self.zones_in_chunk()

        self.mobs = None
        self.objects = None
        self.structures = None

    def __str__(self):
        return f"x_start: {self.x_start}; y_start: {self.y_start}\nx_end: {self.x_end}; y_end: {self.y_end}"

    def zones_in_chunk(self):
        return [zone for zone in self.manager.world.zone_manager.zones if zone.shape.intersects_with(self)]
