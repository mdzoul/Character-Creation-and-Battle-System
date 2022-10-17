import random
import os
import time
import math


race_list = ["Human", "Elf", "Ogre", "Orc", "Dragon", "Goblin", "Dryad"]


def roll_dice(sides):
    return random.randint(1, sides)

def health_stat():
    health = math.ceil((roll_dice(6) * roll_dice(12)) / 2 + 10)
    return health

def strength_stat():
    strength = math.ceil((roll_dice(6) * roll_dice(8)) / 2 + 12)
    return strength

def build_char():
    name = input("\nName your Hero:\n").title()

    race_chosen = False
    while not race_chosen:
        global race_list
        race = input("\nCharacter Race\n(Human, Elf, Ogre, Orc, Dragon, Goblin, Dryad):\n").title()
        if race in race_list:
            break
        else:
            print("\33[31mRace does not exist. Pick another race.\33[0m")
            time.sleep(1)
    
    time.sleep(1)
    print(f"\n\33[1;34m{name} of the {race} race\33[0m")
    time.sleep(1)
    health = health_stat()
    print(f"HEALTH: \33[32m{health}\33[0m")
    time.sleep(1)
    strength = strength_stat()
    print(f"STRENGTH: \33[32m{strength}\33[0m")
    time.sleep(1)
    return name, race, health, strength

def battle_phase(hero_1_hp, hero_2_hp):
    hero_1_roll = roll_dice(6)
    hero_2_roll = roll_dice(6)
    if hero_1_roll > hero_2_roll:
        dmg = roll_dice(hero_1_str)
        print(f"\33[1m{hero_1}\33[0m attacks!")
        print(f"{hero_2} takes a hit, with \33[4;31m{dmg}\33[0m damage!")
        hero_2_hp -= dmg
    elif hero_2_roll > hero_1_roll:
        dmg = roll_dice(hero_2_str)
        print(f"\33[1m{hero_2}\33[0m attacks!")
        print(f"{hero_1} takes a hit, with \33[4;31m{dmg}\33[0m damage!")
        hero_1_hp -= dmg
    else:
        print("Both heroes missed!")
    return hero_1_hp, hero_2_hp

def update_hp():
    time.sleep(1)
    print(f"\n\33[1;34m{hero_1} of the {hero_1_race} race\33[0m")
    time.sleep(1)
    print(f"HEALTH: \33[32m{hero_1_hp}\33[0m")

    time.sleep(1)
    print(f"\n\33[1;34m{hero_2} of the {hero_2_race} race\33[0m")
    time.sleep(1)
    print(f"HEALTH: \33[32m{hero_2_hp}\33[0m")
    

create_char = True
while create_char:
    os.system("clear")
    print("⚔️ CHARACTER BUILDER ⚔️")
    time.sleep(1)
    
    hero_1, hero_1_race, hero_1_hp, hero_1_str = build_char()
    
    print("\nWho are they battling?: ")
    
    hero_2, hero_2_race, hero_2_hp, hero_2_str = build_char()
    
    ready_battle = input("\nReady for battle?: ").lower()
    if ready_battle == "no":
        pass
    elif ready_battle == "yes":
        create_char = False

rounds = 0
battling = True
while battling:
    os.system("clear")
    print("⚔️ BATTLE ⚔️\n")
    time.sleep(1)

    rounds += 1
    
    print("The battle begins!\n")
    time.sleep(1)
    print(f"\33[1;4mROUND {rounds}\33[0m")
    time.sleep(1)    
    
    hero_1_hp, hero_2_hp = battle_phase(hero_1_hp, hero_2_hp)

    update_hp()

    if hero_1_hp < 1:
        battling = False
        winner, winner_race = hero_2, hero_2_race
        loser, loser_race = hero_1, hero_1_race
        print(f"\nOh no! \33[1;34m{loser}\33[0m has died!")
        time.sleep(1)
        input("\nHit [Enter] to continue")
    elif hero_2_hp < 1:
        battling = False
        winner, winner_race = hero_1, hero_1_race
        loser, loser_race = hero_2, hero_2_race
        print(f"\nOh no! \33[1;34m{loser}\33[0m has died!")
        time.sleep(1)
        input("\nHit [Enter] to continue")
    else:
        time.sleep(1)
        print("\nLooks like they're both standing for the next round!")
        time.sleep(1)
        input("\nHit [Enter] to continue")

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE ⚔️\n")
time.sleep(1)

print(f"\33[1;34m{winner} of the {winner_race} race\33[0m destroyed \33[1;34m{loser} of the {loser_race} race\33[0m in \33[1m{rounds}\33[0m round(s)!")