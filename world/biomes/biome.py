class Biome:

    def __init__(self):
        self.name = "Name"
        self.altitude = 0
        self.temperature = 0
        self.passability = 0
        self.bg_color = (0, 0, 0)


class Range:

    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def __call__(self, number):
        return self.in_range(number)

    def in_range(self, number):
        return self.min <= number < self.max


class Ocean(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Name"
        self.temperature = 0
        self.passability = 1
        self.bg_color = (0, 0, 255)


class Land(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Name"
        self.temperature = 0
        self.passability = 0
        self.bg_color = (0, 255, 0)
