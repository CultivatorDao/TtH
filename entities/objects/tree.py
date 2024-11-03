from .object import Object


class Tree(Object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Tree"
        self.icon = "T"
        self.set_position(10, 10)
        self.create_dialogue()
