from .. import Item

class Consumable(Item):
    """Consumable class
    
    Derives from Item, comes out of the box with effects and misc attributes for consumable creation

    Attributes:
        effects: list of effects triggered on consumable use
        duration: int, duration of the effects (in seconds). 0 means instant effects. Defaults to 60
        uses_left: int, how many uses are left on the consumable. Defaults to 1"""
    def __init__(self, effects: list = [], duration: float = 60, uses: int = 1, **kwargs) -> None:
        self.effects = effects
        self.duration = duration #In seconds
        self.uses_left = uses

        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Consumable({self.name} - {self.effects} for {self.duration}s)>"

