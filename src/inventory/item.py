from ..signals import Signal

class Item:
    """Base item class.

    Meant to be used as a way to store data concerning items

    Attributes:
        count: Integer, quantity of item stored, mostly used for inventory management
        stackable: Boolean, defines whether or not items of the same typed can be grouped in inventory
    """
    count = 1
    stackable = True
    durability = None
    def __init__(self, name) -> None:
        self.destroyed = Signal()
        self.name = name

    def __repr__(self):
        return f"<Item({self.name})>"

    def destroy(self):
        self.destroyed.fire(self)
