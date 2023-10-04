
class Item:
    """Base item class.

    Meant to be used as a way to store data concerning items

    Attributes:
        count: Integer, quantity of item stored, mostly used for inventory management
        stackable: Boolean, defines whether or not items of the same typed can be grouped in inventory
    """
    count = 1
    stackable = True
    def __init__(self) -> None:
        pass
