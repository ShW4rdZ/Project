from ..signals import Signal

class Item:
    """Base item class.

    Meant to be used as a way to store data concerning items

    Attributes:
        name: str, display name of the item
        destroyed: Signal, triggered on item destruction
    """
    def __init__(self, name: str = "Dummy") -> None:
        self.destroyed = Signal()
        self.name = name

    def __repr__(self) -> str:
        return f"<Item({self.name})>"

    def destroy(self) -> None:
        """Removes this item from its attached inventory if it added to one
        .. Note::
            The item instance itself is not destroyed, it's only removed from the inventories it was in
        """
        self.destroyed.fire(self)

