import random

class Hero:
    def __init__(self, name, classe):
        self.name = name
        self.hero_class = classe.lower()
        self.moves = {"attack":self.attack}

        if classe.lower() == "barbarian":
            self.health = 150
            self.attack_power = 30
            self.mana = 0
            self.evade = 0
            self.rage_cool = 2
            self.rage_bonus = 10
            self.moves["rage"] = self.rage
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

    def move(self):
        for i in self.moves:
            print(i)
        print(self.name)
        move = input(f"what will {self.name} do?: ").lower()
        for i in self.moves:
            if move == i:
                self.moves[i]
                
    def rage(self,_input):
        self.attack(self.rage_bonus)
    
    def is_alive(self):
        return self.health > 0

    def attack(self, bonus):
        print(f"hello {bonus}")