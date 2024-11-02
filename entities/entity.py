import components


class Entity:

    def __init__(self, world):
        self.world = world
        self.name = ""
        self.icon = " "
        self.position = components.PositionComponent(parent=self)

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y
