import components


class Entity:

    def __init__(self, world=None, x=0, y=0):
        self.world = world
        self.name = ""
        self.icon = " "
        self.position = components.PositionComponent(parent=self, x=x, y=y)
        self.frequency = 10

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y
