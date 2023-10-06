from src.inventory import Inventory, Item
from src.player import Player
from src.database import save, load

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
    
    #sword.destroy()
    print(game.player.inventory)

    #save(game, "game")
    g_load = load("game")
    print(g_load)
    print(g_load.player.inventory)
    g_load.player.inventory.clear()
    print(g_load.player.inventory)
