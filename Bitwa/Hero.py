from abc import abstractmethod, ABC


class Hero(ABC):
    def __init__(self, name: str, damage: float, health: float, mana: float, money: int):
        self.name = name
        self.damage = damage
        self.health = health
        self.mana = mana
        self.money = money

    def __str__(self):
        return f"{self.name}, health: {self.health},money: {self.money}, mana: {self.mana}"

    def rest(self):
        if self.is_alive():
            self.mana += 10
            return
        print(f"{self.name} is dead!")

    def basic_atack(self, other):
        if self.is_alive():
            other.health -= self.damage
            return
        print(f"{self.name} is dead!")

    def rob(self, other):
        if self.is_alive():
            self.money += other.money
            other.money = 0
            return
        print(f"{self.name} is dead!")

    def is_alive(self) -> bool:
        if self.health >= 0:
            return True
        return False

    @abstractmethod
    def special_attack(self, other):
        pass
