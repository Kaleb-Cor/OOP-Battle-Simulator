from hero import Hero
from goblin import Goblin
import random

def order(round: list):
    order = []
    for character in round:
        character.order = random.randint(1,20)
        if order.len() >= 1:
            for i in order:
                if i.order < character.order:
                    order.insert(order.index(i),character)
        else:
            order.append(character)

def battle(order: list):
    for character in order:
        if isinstance(character,Hero):
            if character.is_alive():
                character.move()
        else:
            for i in order:
                if isinstance(i,Hero):
                    character.attack()
    

