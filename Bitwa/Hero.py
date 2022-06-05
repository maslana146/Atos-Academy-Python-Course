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
        self.mana += 10

    def basic_atack(self, other):
        other.health -= self.damage

    def rob(self, other):
        self.money += other.money
        other.money = 0

    @abstractmethod
    def special_attack(self, other):
        pass
