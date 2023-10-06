from . import Equipment

class Weapon(Equipment):
    """Weapon class that derives from Equipment, helps with creating weapons"""
    def __init__(self, **kwargs) -> None:
        
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Weapon({self.name} - {self.durability}/{self.max_durability})>"
