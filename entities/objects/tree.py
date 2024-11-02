from .object import Object


class Tree(Object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = "#"
        self.set_position(3, 4)
