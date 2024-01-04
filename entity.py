import abc


class Entity(abc.ABC):
  """
  Entity is an Abstract class:
  Attributes: _name – entity’s name, _hp – entity’s hit points, _max_hp – entity’s starting hp.  
  """

  def __init__(self, name, max_hp):
    """ set the _name, _max_hp, and _hp. Assign the max_hp value
    to both the _max_hp and _hp attributes."""
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    """ Use decorators to create the properties for the name """
    return self._name

  def hp(self):
    """ Use decorators to create the properties for the hp """
    return self._hp

  def take_damage(self, dmg):
    """ the damage the entity takes, if hp’s a negative value, reset it to 0 """
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """ display the entity’s name and hp in the format “Name: hp/max_hp”. """
    return f"{self._name}: ({self._hp}/{self._max_hp})"

  @abc.abstractmethod
  def basic_attack(self, other):
    """ abstract method, will be overridden by child classes  """
    pass

  @abc.abstractmethod
  def special_attack(self, other):
    """ abstract method, will be overridden by child classes  """
    pass
