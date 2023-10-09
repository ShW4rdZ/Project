from src.inventory import Inventory, Item, Equipment, Consumable, Weapon, StackableItem
from src.player import Player
#from src.database import save, load 

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

    sword = Weapon(name = "Rusty Sword", max_durability = 72)
    shield = Equipment(name = "Shield", max_durability = 420)
    shield.damage(400)
    shield.repair(30)
    sword.damage(3)

    potion = Consumable(name = "Dungeon potion", effects = ["Regeneration", "Strength"], duration = 2)
    coins = StackableItem(name = "Coins", count = 70531)
    coins.add_count(10000)
    coins.remove_count(11111)

    print(sword, shield, potion, coins, "\n")
    
    game.player.inventory.add(sword, shield, potion, coins)
    print(game.player.inventory, "\n")
    
    sword.destroy()
    print(game.player.inventory, "\n")

    #save(game, "game")
    #g_load = load("game")
    #print(g_load)
    #print(g_load.player.inventory)
    #g_load.player.inventory.clear()
    #print(g_load.player.inventory)
