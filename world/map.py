class Map:

    def __init__(self,
                 engine,
                 width=30,
                 height=30,
                 ):
        self.engine = engine
        self.width = width
        self.height = height

    def show_map(self):
        for y in range(self.height):
            for x in range(self.width):
                print("0", end="")
            print()

    def execute(self, command):
        switch
