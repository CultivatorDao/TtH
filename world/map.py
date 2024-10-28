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

        self.character_position = self.engine.character.position

    def display_object(self, x, y):
        icon = ""
        for obj in self.world.all_objects:
            if x == obj.position.x and y == obj.position.y:
                icon = obj.icon
                break
            else:
                icon = "0"

        print(icon, end=" ")

    def show_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self.display_object(x, y)
            print()

    def check_collisions(self, x, y):
        pass

    def character_sight(self):
        position = self.character_position.position
        print(position)
        for y in range(position[1] - 2, position[1] + 3):
            for x in range(position[0] - 2, position[0] + 3):
                self.display_object(x, y)
            print()

    def move(self, x, y):
        self.character_position.move(x, y)
        self.character_sight()
