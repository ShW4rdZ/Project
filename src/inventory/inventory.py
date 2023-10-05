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

    def add(self, *items) -> None:
        for item in items:
            item.destroyed.connect(self.on_destroyed)
            self._items.append(item)

    def on_destroyed(self, item) -> None:
        self._items.remove(item)



