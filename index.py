from src.inventory import Inventory, Item
from src.player import Player


class Game:
    def __init__(self) -> None:
        print("######\nRPyG\n######")
    def start(self) -> None:
        print("Loading player")
        self.player = Player() 

        print("Starting game !")

if __name__ == "__main__":
    game = Game()
    game.start()

    sword = Item("Sword")
    shield = Item("Shield")
    print(sword, shield)
    
    game.player.inventory.add(sword, shield)
    print(game.player.inventory)
    
    sword.destroy()
    print(game.player.inventory)
