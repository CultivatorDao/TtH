from ..entity import Entity
from state.dialogue import Dialogue


class Object(Entity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialogue = None

    def create_dialogue(self):
        self.dialogue = Dialogue(engine=self.world.engine,
                                 message=f"You approached {self.name}. Your actions:", instructions=[
                                    ["1", "Destroy", self.destroy],
                                    ], can_skip=True
                                 )

    def destroy(self):
        pass
