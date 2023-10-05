from .item import Item

class Inventory:
    """Base inventory class.

    Meant to be used as an inventory to store data on entities

    Attributes:
        contents: A list of Item classes storing items contained in the inventory
    """
    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return f"<Inventory({self._items})>"

    def add(self, *items: Item) -> None:
        """Adds any number of items to the inventory"""
        for item in items:
            item.destroyed.connect(self._on_destroyed)
            self._items.append(item)

    def _on_destroyed(self, item) -> None:
        """Removes inputted item from the inventory"""
        self._items.remove(item)



