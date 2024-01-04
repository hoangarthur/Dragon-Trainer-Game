from abc import abstractmethod
import entity
import random


class Hero(entity.Entity):
  """
  Hero Class – inherits from Entity: 
  1. override basic_attack(self, other) of the class Entity.
  2. override special_attack(self, other) of the class Entity. 
  """

  def basic_attack(self, other):
    """the other entity (the dragon) takes a random amount of
       damage in the range 2D6 (1-6 + 1-6). 
       => Return a string with the description of the attack and 
       the damage dealt to the dragon. """
    dmg = random.randint(1, 6) + random.randint(1, 6)
    other.take_damage(dmg)
    return f"\nYou slash the {other._name} with your sword for {dmg} damage."

  def special_attack(self, other):
    """the other entity (the dragon) takes a random amount
       of damage in the range 1D12 (1-12).
       => Return a string with the description of the attack
       and the damage dealt to the dragon. """
    dmg = random.randint(1, 12)
    other.take_damage(dmg)
    return f"You hit the {other._name} with your bow for {dmg} damage."
