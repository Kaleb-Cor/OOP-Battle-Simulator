from random import *
from enemy import enemy

class boss(enemy):
    def __init__(self, name, health=200, attack_power=20):
        super().__init__(name, health, attack_power)
        self.armor = 1.4

    def attack(self):
        attack_style=randint(1,3)

        if attack_style == 1:
            return randint(1,6) + randint(1,6) + randint(1,6)
        
        elif attack_style == 2:
            return randint(5,10)

        else:
            return randint(1,20) + randint(1,20)

    def take_damage(self, attack):
        damage = attack/self.armor
        super().take_damage(damage)