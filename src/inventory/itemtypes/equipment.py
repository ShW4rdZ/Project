from .. import Item

class Equipment(Item):
    """Base equipment class
    
    Derives from Item, comes out of the box with durability and other functions to ease the process of creating equipment items

    Attributes:
        max_durability: int, base durability of the equipment piece
        durability: int, current durability of the equipment piece
    """
    def __init__(self, max_durability: int = 1, **kwargs) -> None:
        self.max_durability = max_durability
        self.durability = self.max_durability

        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Equipment({self.name} - {self.durability}/{self.max_durability})>"

    def damage(self, damage: int = 1) -> int:
        """Reduces durability of equipment. If new durability is below 0, destroy the item. Returns the new durability"""
        self.durability -= damage
        if self.durability < 0:
            self.destroy()
        return self.durability

    def repair(self, damage: int = -1) -> int:
        """Repairs <damage> amount of damage on the equipment. If <damage> < 0, restores fully the durability. Returns the new durability"""
        if damage < 0:
            self.durability = self.max_durability
        else:
            self.durability += damage
            if self.durability > self.max_durability:
                self.durability = self.max_durability
        return self.durability

