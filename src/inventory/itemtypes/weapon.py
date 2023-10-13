from . import Equipment

class Weapon(Equipment):
    """Weapon class:

    Derives from Equipment, helps with creating weapons

    Attributes:
        attack_speed: float, attack speed of the weapon (attack_speed attacks per second)
    """
    def __init__(self, attack_speed: float = 1, **kwargs) -> None:
        self.attack_speed = attack_speed # Attack speed: attack_speed attacks per second
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Weapon({self.name} - {self.durability}/{self.max_durability})>"
