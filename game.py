from goblin import Goblin
from hero import Hero
from system import *

ARENA_NAME = "THE BASEMENT"

def main():
    #Open the arena and introduce its first opponent.
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Claire")
    goblin2= Goblin("Andrew")
    hero = Hero("Jason", "barbarian")

    print("")
    print(f"{goblin.name} enters {ARENA_NAME} with {goblin.health} health.")
    print(f"{goblin2.name} enters {ARENA_NAME} from Claire's house with {goblin2.health} health.")

    print("")
    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")
    print("")

    #Intro Over Run Game Here
    hero.move()

    
if __name__ == "__main__":
    main()
