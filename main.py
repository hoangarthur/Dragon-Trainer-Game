"""
  Description: Dragon Trainer - a game where the user must defeat three dragons to pass the trail.
"""

import check_input
import random
import entity
from hero import Hero
from dragon import Dragon
import fire_dragon
import flying_dragon


def main():
  """
  Welcome messages and inform the player of the game's objective.
  Initialize the player/hero and 3 dragons/computer.
  """
  name = input("What is your name, challenger?\n")
  hero = Hero(name, 50)
  drag_list = [
      Dragon("Deadly Nadder", 10),
      fire_dragon.FireDragon("Gronckle", 15, 3),
      flying_dragon.FlyingDragon("Timberjack", 20, 5)
  ]

  print(f"Welcome to dragon training, {name} \nYou must defeat 3 dragons.\n")

  while (len(drag_list) > 0):
    print(f"{hero}")
    for i in range(1, len(drag_list) + 1):
      print(f"{i}. Attack {drag_list[i-1]}")
    """ Prompts the user to select a dragon to fight and the weapon used to fight."""

    dragonToAttack = check_input.get_int_range("Choose a dragon to attack: ",
                                               1, len(drag_list))
    attackWeapon = check_input.get_int_range(
        "\nAttack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon: ", 1,
        2)
    """ The computer will randomly generate attacks from randomized dragons. """
    dragon_attack = random.randint(1, 2)
    if (attackWeapon == 1):
      print(hero.basic_attack(drag_list[dragonToAttack - 1]))
    else:
      print(hero.special_attack(drag_list[dragonToAttack - 1]))
    if (drag_list[dragonToAttack - 1]._hp > 0):
      if dragon_attack == 1:
        print(drag_list[dragonToAttack - 1].basic_attack(hero))
      else:
        print(drag_list[dragonToAttack - 1].special_attack(hero))

    if drag_list[dragonToAttack - 1]._hp < 1:
      print(f"\nYou defeated {drag_list[dragonToAttack-1]._name}!\n")
      drag_list.pop(dragonToAttack - 1)

    if (hero._hp == 0):
      """The player/hero lose if the hp go below or 0 and the game terminates"""
      print("You lose!")
      break
    elif (len(drag_list) == 0):
      """If player defeated 3 dragons, the dragon list is empty. 
    Print the congrats message and end the game"""
      print(
          "Congratulations! You have defeated all 3 dragons, you have passed the trials."
      )


main()
