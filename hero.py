import random

class Hero:
    def __init__(self, name, classe):
        self.name = name
        self.health = 120
        self.attack_power = 20
        self.hero_class = classe

    def attack(self):
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage, attacker):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage from {attacker.name}. Health: {self.health}")
    
    def is_alive(self):
        return self.health > 0
