from .item import Item

class Inventory:
    """Base inventory class.

    Meant to be used as an inventory to store data on entities

    Attributes:
        contents: A list of Item classes storing items contained in the inventory
    """
    def __init__(self, item_list: list[Item] = None) -> None:
        self.contents = []
        if not item_list is None and type(item_list) == list:
            self.contents += item_list

    def add_item(self, item : Item, count: int = 1) -> None:
        """Adds an item to the inventory, adds it to the item count if item is stackable"""
        assert type(item) == Item, "item must be an instance of the Item class !"
        if item in self.contents and item.stackable: # Will need to change the way wa detect items in inventory
            self.contents[self.contents.index(item)].count += count
        else:
            self.contents.append(item)



