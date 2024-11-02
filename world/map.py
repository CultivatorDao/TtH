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
        return [obj for obj in self.world.all_objects
                if
                (self.character_position.x - self.character.eyesight) <
                obj.position.x < self.character_position.x + self.character.eyesight + 1
                and
                self.character_position.y - self.character.eyesight < obj.position.y <
                self.character_position.y + self.character.eyesight + 1
                ]

    def display_object(self, x, y):
        icon = ""
        for obj in self.objects_in_sight:
            if x == obj.position.x and y == obj.position.y:
                icon = obj.icon
                break
            else:
                icon = "~"

        print(icon, end=" ")

    def show_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self.display_object(x, y)
            print()

    def check_collisions(self):
        for obj in self.world.all_objects:
            if (self.character_position.x == obj.position.x and self.character_position.y == obj.position.y) \
                    and obj.icon != "@":
                self.engine.dialogue = obj.dialogue
            else:
                continue

    def character_sight(self):
        position = self.character_position.position
        print(self.character_position)
        for y in range(position[1] - self.character.eyesight, position[1] + self.character.eyesight + 1):
            for x in range(position[0] - self.character.eyesight, position[0] + self.character.eyesight + 1):
                if x == position[0] - self.character.eyesight:
                    print(" " * 30, end="")
                self.display_object(x, y)
            print()

    def move(self, x, y):
        self.character_position.move(x, y)
        self.check_collisions()

