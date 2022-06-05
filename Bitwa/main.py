import random
from typing import List

from Bitwa.Batman import Batman
from Bitwa.Hero import Hero
from Bitwa.Hulk import Hulk

hulk = Hulk('Hulk', 10, 200, 10, 1000)

batman = Batman('Batman', 25, 120, 20, 1000)
heros: List[Hero] = [batman, hulk]

while True:
    hero = random.choice(heros)
    if not hero.is_alive():
        print(f"{hero.name} is dead!")
        break
    if isinstance(hero, Batman):
        victim = hulk
    else:
        victim = batman
    attack: int = random.randint(1, 3)
    if attack == 1:
        print(f"{hero.name} atakuje {victim.name} podstawowym atakiem!")
        hero.basic_atack(victim)
    else:
        print(f"{hero.name} atakuje {victim.name} specialnym atakiem!")
        hero.special_attack(victim)
