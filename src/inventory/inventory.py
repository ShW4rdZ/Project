"""Inventory class"""
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

    def clear(self) -> None:
        """Clears the inventory"""
        self._items = []

    def _on_item_destroyed(self, item) -> None:
        """Removes inputted item from the inventory"""
        self._items.remove(item)

    def __iter__(self):
        self.iter_data = self._items[:]
        return self

    def __next__(self):
        if not self.iter_data:
            raise StopIteration
        return self.iter_data.pop()
