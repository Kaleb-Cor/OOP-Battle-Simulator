from goblin import Goblin
from hero import Hero


ARENA_NAME = "THE BASEMENT"


def main():
    #Open the arena and introduce its first opponent.
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Claire")
    goblin2= Goblin("Andrew")
    hero = Hero("Jason", "Barbarian")

    print("")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} Enters the Arena from claires house with {goblin2.health} health.")

    print("")
    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")
    print("")

    goblin2.take_damage(hero.attack())
    hero.take_damage(goblin.attack(),goblin)
    
if __name__ == "__main__":
    main()
