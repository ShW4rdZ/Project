from .item import Item

class Inventory:
    """Base inventory class.

    Meant to be used as an inventory to store data on entities
    """
    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return f"<Inventory({self._items})>"

    def add(self, *items: Item) -> None:
        """Adds any number of items to the inventory"""
        for item in items:
            item.destroyed.connect(self._on_item_destroyed)
            self._items.append(item)

    def _on_item_destroyed(self, item) -> None:
        """Removes inputted item from the inventory"""
        self._items.remove(item)

    def clear(self) -> None:
        """Clears the inventory"""
        self._items = []


