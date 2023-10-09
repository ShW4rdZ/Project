from .. import Item

class StackableItem(Item):
    """Stackable item class
    
    Derives from Item, comes out of the box with count and methods to manage stackable items
    """
    def __init__(self, count: int = 1, **kwargs) -> None:
        self._count = count

        super().__init__(**kwargs)

    def add_count(self, count: int) -> int:
        """Adds count to the current quantity of the item. Returns the new quantity"""
        self._count += count
        return self._count

    def remove_count(self, count: int) -> int:
        """Removes count items from the current quantity of the item. Returns the new quantity"""
        self._count -= count
        if self._count < 0:
            self._count = 0
        return self._count

    def get_count(self) -> int:
        return self._count

    def __repr__(self) -> str:
        return f"<StackableItem({self.name} * {self._count})>"
