from Bitwa.Hero import Hero


class Hulk(Hero):
    def __init__(self, name: str, damage: float, health: float, mana: float, money: int):
        super().__init__(name, damage, health, mana, money)

    def special_attack(self, other):
        if self.is_alive():
            other.health -= self.damage * 1.5
            self.health += self.health * 1.5
            return
        print(f"{self.name} is dead!")
