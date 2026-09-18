from goblin import Goblin
from hero import Hero

ARENA_NAME = "THE BASEMENT"

def battle(hero: Hero, enemy: Goblin):
    round = 1

    while hero.is_alive() and enemy.is_alive():
        print(f"\nROUND {round}. FIGHT")
        enemy.take_damage(hero.attack())
        if enemy.is_alive():
            hero.take_damage(enemy.attack(), enemy)
        round += 1
    if hero.is_alive():
        print(f"{hero.name} wins with {hero.health} health")
    else:
        print(f"{hero.name} has lost")

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

    battle(hero, goblin2)
    battle(hero, goblin)
    
if __name__ == "__main__":
    main()
