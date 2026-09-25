import random

from enemy import enemy

class Goblin(enemy):
    #"""A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name,100,10)
        self.gold = 0

    def steal_gold(self, target):
        gold = random.randint(5,10)
        if gold > target.gold:
            self.gold += target.gold
            target.gold = 0
        else:
            self.gold += gold
            target.gold -= gold
