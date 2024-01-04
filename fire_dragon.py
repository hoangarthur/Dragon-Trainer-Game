import dragon
import random


class FireDragon(dragon.Dragon):
  """
  1. Inherits from Dragon class.
  2. Has an extra attribute for shots.
  3. Overrides init and calls super.
  4. Overrides str method and calls super.
  5. Overrides special_attack method, does damage, 
  decrements shots, and returns attack string.
  """

  def __init__(self, name, max_hp, f_shots):
    """call super init to set the name and hp, then set the number of fire_shots."""
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  def special_attack(self, other):
    """ overridden fire attack """
    if (self.f_shots >= 1):
      dmg = random.randint(5, 9)
      other.take_damage(dmg)
      self.f_shots -= 1
      return f"{self._name} engulfs you in flames for {dmg} damage!\n"

  def __str__(self):
    """ get the __str__ from entity class and display number of fire shots"""
    dragon_info = super().__str__()
    return f"{dragon_info}\nFire Shots remaining: {self.f_shots}"
