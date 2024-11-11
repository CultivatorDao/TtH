class Map:

    def __init__(self,
                 world,
                 width=30,
                 height=30,
                 ):
        self.world = world
        self.engine = self.world.engine
        self.width = width
        self.height = height

        self.character = self.world.character
        self.character_position = self.character.position

    @property
    def objects_in_sight(self):
        _x = self.character_position.x
        _y = self.character_position.y
        eyesight = self.character.eyesight

        return [obj for obj in self.world.all_objects
                if (_x - eyesight * 2 - 1) < obj.position.x < _x + eyesight * 2 + 1
                and
                _y - eyesight * 2 - 1 < obj.position.y < _y + eyesight * 2 + 1]

    def display_object(self, x, y):
        icon = "~"
        for obj in self.objects_in_sight:
            if x == obj.position.x and y == obj.position.y:
                icon = obj.icon
                break

        print(icon, end=" ")

    # def show_map(self):
    #     for y in range(self.height):
    #         for x in range(self.width):
    #             self.display_object(x, y)
    #         print()

    def check_boundaries(self, x, y):
        if 0 <= x < self.width + 1 and 0 <= y < self.height + 1:
            return True
        else:
            return False

    def check_collisions(self):
        _x = self.character_position.x
        _y = self.character_position.y

        for obj in self.world.all_objects:
            if (_x == obj.position.x and _y == obj.position.y) and obj.icon != "@":
                self.engine.dialogue = obj.dialogue
            else:
                continue

    def create_offset(self, character):
        """
        Creates offset with player in center. With respect of player's sight.
        :param character: object
        :return: (int, int, int, int)
        """
        y_start = character.position.y - character.eyesight
        y_end = character.position.y + character.eyesight
        x_start = character.position.x - character.eyesight
        x_end = character.position.x + character.eyesight
        # Offset alignment
        if y_start <= 0:
            y_end += abs(0 - y_start)
            y_start = 0
        if x_start <= 0:
            x_end += abs(0 - x_start)
            x_start = 0
        if y_end > self.height:
            y_start -= abs(self.height - y_end)
            y_end = self.height
        if x_end > self.width:
            x_start -= abs(self.width - x_end)
            x_end = self.width

        # Trace player location and player sight borders
        # print(f"y_start: {y_start}   y_end: {y_end}   x_start: {x_start}   x_end: {x_end}")
        # print(f"Player_x: {player.x}   Player_y: {player.y}")

        return y_start, y_end, x_start, x_end

    def character_sight(self):
        y_start, y_end, x_start, x_end = self.create_offset(self.character)
        print(self.character_position)

        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if x_start == x:
                    print(" " * 40, end="")
                if self.check_boundaries(x, y):
                    self.display_object(x, y)
            print()

    def move(self, x, y):
        _x = self.character_position.x
        _y = self.character_position.y
        if self.check_boundaries(x + _x, y + _y):
            self.character_position.move(x, y)
            self.world.encounter()
        self.check_collisions()

