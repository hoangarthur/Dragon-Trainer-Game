import dragon
import random


class FlyingDragon(dragon.Dragon):
  """
  1. Inherits from Dragon class.
  2. Has an extra attribute for swoops.
  3. Overrides init and calls super.
  4. Overrides str method and calls super.
  5. Overrides special_attack method, does damage, 
  decrements swoops, and returns attack string.
  """

  def __init__(self, name, max_hp, swoops):
    """ set the name, hp, and swoops """
    super().__init__(name, max_hp)
    self.swoops = swoops

  def special_attack(self, other):
    """ overridden swoop attack """
    if (self.swoops > 0):
      dmg = random.randint(5, 8)
      other.take_damage(dmg)
      self.swoops -= 1
      return f"{self._name} smashes you with its tail for {dmg} damage!\n"

  def __str__(self):
    """ get the __str__ from the entity class, then display the number of swoops"""
    dragon_info = super().__str__()
    return f"{dragon_info}\nSwoops attacks remain {self.swoops}"
