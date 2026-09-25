import random

class enemy:
    def __init__(self, name, health=50, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self):
        #"""Return a random amount of damage."""
        return random.randint(1, self.attack_power)
        
    def take_damage(self, damage):
        #"""Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        
    def is_alive(self):
        #"""Return True while the enemy has health remaining."""
        return self.health > 0
    