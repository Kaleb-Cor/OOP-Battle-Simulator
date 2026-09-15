import random

class Hero:
    def __init__(self, name, classe):
        self.name = name
        
        self.hero_class = classe

        if classe.lower() == "barbarian":
            self.health = 150
            self.attack_power = 30
            self.mana = 0
            self.evade = 0
        elif classe.lower() == "wizard":
            self.health = 100
            self.attack_power = 20
            self.mana = 100
            self.evade = 0
        elif classe.lower() == "rogue":
            self.health = 120
            self.attack_power = 20
            self.mana = 0
            self.evade = 10

    def attack(self):
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage, attacker):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage from {attacker.name}. Health: {self.health}")
    
    def is_alive(self):
        return self.health > 0
