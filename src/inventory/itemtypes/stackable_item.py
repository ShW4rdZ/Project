"""Stackable item class"""
from .. import Item

class StackableItem(Item):
    """Stackable item class

    Derives from Item, comes out of the box with count and methods to manage stackable items
    """
    def __init__(self, count: int = 1, **kwargs) -> None:
        self._count = count

        super().__init__(**kwargs)

    @property
    def count(self) -> int:
        """Property: quantity of the item"""
        return self._count

    @count.setter
    def count(self, count: int) -> None:
        """Set the quantity of the item"""
        if count < 0:
            raise ValueError("Item quantity cannot be negative !")
        self._count = count

    def __repr__(self) -> str:
        return f"<StackableItem({self.name} * {self._count})>"
