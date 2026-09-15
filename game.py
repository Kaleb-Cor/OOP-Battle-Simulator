from goblin import Goblin
from hero import Hero

ARENA_NAME = "THE BASEMENT"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        enemy.take_damage(hero.attack())
        if enemy.is_alive():
            hero.take_damage(enemy.attack(), enemy)
    if hero.is_alive():
        print(f"{hero.name} wins")
    else:
        print(f"{hero.name} has lost")

def main():
    #Open the arena and introduce its first opponent.
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Claire")
    goblin2= Goblin("Andrew")
    hero = Hero("Jason", "rogue")

    print("")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} Enters the Arena from claires house with {goblin2.health} health.")

    print("")
    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")
    print("")

    battle(hero, goblin2)
    
if __name__ == "__main__":
    main()
