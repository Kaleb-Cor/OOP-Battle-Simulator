import random

class Hero:
    def __init__(self, name, classe):
        self.name = name
        self.hero_class = classe.lower()

        if classe.lower() == "barbarian":
            self.health = 150
            self.attack_power = 30
            self.mana = 0
            self.evade = 0
            self.rage = False
        elif classe.lower() == "wizard":
            self.health = 100
            self.attack_power = 20
            self.mana = 100
            self.evade = 0
        elif classe.lower() == "rogue":
            self.health = 130
            self.attack_power = 20
            self.mana = 0
            self.evade = 10
        elif classe.lower() == "paladin":
            self.health = 140
            self.attack_power = 20
            self.mana = 20
            self.evade = 0
        elif classe.lower() == "cleric":
            self.health = 130
            self.attack_power = 10
            self.mana = 100
            self.evade = 0

    def attack(self):
        attack_bonus = 0
        if self.hero_class == "wizard" or self.hero_class == "paladin":
            attack_bonus = random.randint(0,self.mana)
            self.mana -= attack_bonus
        if self.hero_class == "barbarian":
            if self.rage == True:
                print(f"{self.name} is ENRAGED")
                attack_bonus += 10
                self.rage = False
        return random.randint(1, self.attack_power) + attack_bonus
    
    def take_damage(self, damage, attacker):
        if self.hero_class == "barbarian" and random.randint(1,20) <= 3:
            self.rage = True
        if random.randint(1, 100) > self.evade:
            self.health = max(0, self.health - damage)
            print(f"{self.name} takes {damage} damage from {attacker.name}. Health: {self.health}")
        else:
            print(f"{self.name} dodges {attacker.name}'s attack")
    
    def is_alive(self):
        return self.health > 0