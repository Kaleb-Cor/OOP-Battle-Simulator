import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15

    def attack(self):
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage, attacker):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage from {attacker.name}. Health: {self.health}")
    
    def is_alive(self):
        return self.health > 0
