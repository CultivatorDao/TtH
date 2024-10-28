from .base_component import BaseComponent


class CultivationComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cultivation_lvl = 1
