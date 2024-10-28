from .base_component import BaseComponent
import random


class LifespanComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.life_span = 200
        self.max_age = random.randrange(70, 90)
        self.life_span_modifier = 1
        self.year = 18
        self.month = 0
        self.week = 0
        self.day = 0
        self.hour = 0
