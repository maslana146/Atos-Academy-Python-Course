from Bitwa.Hero import Hero


class Batman(Hero):
    def __init__(self, name: str, demage: float, health: float, mana: float, money: int):
        super().__init__(name, demage, health, mana, money)

    def special_attack(self, other):
        other.health -= self.damage * 2
        self.health -= self.damage * 0.1
