import random
from colorama import Fore
import time

cheat_counter = 0
p_health = 100
p_damage = 10
x_health = 150
x_damage = 15

strength_potion = 1
health_potion = 1
potion_effect = False


def attack():
    global x_health, potion_effect
    crit = ["0", "0", "0", "1", "2"]
    crit_chance = random.choice(crit)
    if crit_chance == "0":
        print(Fore.LIGHTBLUE_EX + "You dealt normal damage (-10)")
        p_damage = 10
    elif crit_chance == "1":
        print(Fore.LIGHTGREEN_EX + "You dealt CRITICAL damage (-25)")
        p_damage = 25
    elif crit_chance == "2":
        print(Fore.RED + "You missed...(0)")
        p_damage = 0

    if potion_effect == True:
        p_damage += 15
        potion_effect = False

    x_health -= p_damage
    print(f"Monster health: {x_health}")


def defend():
    global x_damage, p_health
    defend_options = ["0", "1", "2", "3", "0"]
    defense = random.choice(defend_options)

    if defense == "0":
        print("You took normal damage. (-15)")
        x_damage = 15

    elif defense == "1":
        print("You absorbed most of the damage. (-5)")
        x_damage = 5

    elif defense == "2":
        print("You dodged perfectly without taking any damage. (0)")
        x_damage = 0

    elif defense == "3":
        print("Your own sword hit you and the enemy attacked you too. (-25)")
        x_damage = 25

    p_health -= x_damage
    print(f"Your health: {p_health}")


def potion():
    global strength_potion, health_potion, potion_effect, p_health

    print("You have 2 options...")
    time.sleep(0.6)
    print(Fore.RED + "Strength Potion or Health Potion...")
    print("You have 1 of each")
    potion_choice = input("Type health for Health Potion or strength for Strength Potion: ").lower()

    if potion_choice == "strength" and strength_potion > 0:
        strength_potion -= 1
        potion_effect = True

    elif potion_choice == "health" and health_potion > 0:
        health_potion -= 1
        p_health += 21


def death_dice():
    global x_health, p_health, potion_effect

    print("Are you ready for the biggest chaos of your life?")
    time.sleep(0.6)
    x = input("yes or no: ").lower()

    if x == "yes":
        if x_health > p_health:
            if 50 < p_health < 100:
                x_health -= 25
            elif 25 < p_health < 50:
                x_health -= 35
                potion_effect = True
                print(Fore.RED + "POTION EFFECT ACTIVATED!!!")

        elif p_health > x_health:
            if 50 < p_health <= 100:
                p_health -= 30
                potion_effect = True
                print(Fore.RED + "POTION EFFECT ACTIVATED!!!")

            elif 20 < p_health <= 50:
                p_health -= 40

            elif p_health <= 20:
                potion_effect = True
                print(Fore.RED + "POTION EFFECT ACTIVATED!!!")

        elif p_health == x_health:
            x_health -= 25
            p_health -= 30
            potion_effect = True
            print(Fore.RED + "POTION EFFECT ACTIVATED!!!")

    elif x == "no":
        pass


def menu():
    print(Fore.RED + "-" * 30 +
          "\n-------" + Fore.CYAN + " MENU " + Fore.RED + "----------------\n"
          + "-" * 30 +
          "\n-------" + Fore.BLUE + " 1*Attack " + Fore.RED + "-------------\n"
          + "-" * 30 +
          "\n-------" + Fore.BLUE + " 2*Defend " + Fore.RED + "-------------\n"
          + "-" * 30 +
          "\n-------" + Fore.BLUE + " 3*Use Potion " + Fore.RED + "---------\n"
          + "-" * 30 +
          "\n-------" + Fore.BLUE + " 4*Death Dice " + Fore.RED + "---------\n"
          + "-" * 30)


while p_health > 0 and x_health > 0:
    menu()
    choice = input("Which one will you choose? {1-2-3-4}: ")

    if choice == "1":
        attack()
        print("If you use this option twice in a row, the player will execute himself!!!")
        print("You need to defend to prevent the player from executing himself!")
        cheat_counter += 1

        if x_health <= 0:
            print("MONSTER DEFEATED")
            break

        if cheat_counter == 2:
            p_health = 0
            print("The player executed himself, cheater!!!")
            break

    elif choice == "2":
        defend()
        if cheat_counter > 0:
            cheat_counter -= 1

        if p_health <= 0:
            break

    elif choice == "3":
        potion()
        print("Potion used!")
        print(f"Your health: {p_health}")

    elif choice == "4":
        print(Fore.RED + "DEATH DICE!")
        death_dice()

        if x_health <= 0:
            print("Monster defeated...")
            break

        elif p_health <= 0:
            print("The Death Dice consumed your soul and you died...")

    else:
        print("You need to choose 1, 2, 3 or 4!")