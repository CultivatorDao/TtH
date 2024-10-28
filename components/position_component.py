from .base_component import BaseComponent


class PositionComponent(BaseComponent):

    def __init__(self, x=0, y=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
