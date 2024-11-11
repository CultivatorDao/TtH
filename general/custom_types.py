from typing import NewType

from entities import Mob
from state.base_state import State

MobType = NewType("Mob", Mob)
StateType = NewType("State", State)

