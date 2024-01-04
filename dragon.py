import entity
import random


class Dragon(entity.Entity):
  """
  Dragon Class – inherits from Entity:
  1. override basic_attack(self, other) of the class Entity.
  2. override special_attack(self, other) of the class Entity. 
  """

  def basic_attack(self, other):
    """tail attack – the other entity (the hero) takes a random
      amount of damage in the range 3-7.
      => Return a string with the description of the attack 
      and the damage dealt to the hero."""
    dmg = random.randint(3, 7)
    other.take_damage(dmg)
    return f"{self._name} smashes you with its tail for {dmg} damage!\n"

  def special_attack(self, other):
    """claw attack – the other entity (the hero) takes a
      random amount of damage in the range 4-8. 
      => Return a string with the description of the attack
      and the damage dealt to the hero."""
    dmg = random.randint(4, 8)
    other.take_damage(dmg)
    return f"{self._name} slashes you with its claws for {dmg} damage!"
