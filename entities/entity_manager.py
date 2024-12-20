class EntityManager:

    def __init__(self, frequency=0, entities=None, types=None):

        if types is None:
            types = {}
        if entities is None:
            entities = {}

        self.frequency = frequency

        self.entity_types = types
        self.entities = entities

    def __getitem__(self, item):
        return self.entities[str(item)]

    def __setitem__(self, key, value):
        key = str(key)
        if self.entities.get(key):
            self.entities[key].append(value)
        else:
            self.entities[key] = [value]

    def __iter__(self):
        yield from self.entities.items()

    def __add__(self, other):
        return EntityManager(self.entities | other.entities)

    def get(self, key):
        key = str(key)
        return self.entities.get(key)
