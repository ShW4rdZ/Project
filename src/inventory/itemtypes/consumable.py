from .. import Item

class Consumable(Item):
    """Consumable class that derives from Item, comes out of the box with effects and misc attributes for consumable creation"""
    def __init__(self, effects: list = [], duration: float = 1, **kwargs) -> None:
        self.effects = effects
        self.duration = duration

        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Consumable({self.name} - {self.effects} for {self.duration}m)>"

