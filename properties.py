"""
properties is a feature of oops.it enables the class to present vertual attribute.
vertual attribute are normal attribute but they are not actually stored(only readble).
"""

# simple game structure logic  for game
class Character(object):
    def __init__(self,name,max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property          # get the value(only read)
    def hp(self):   # it is read only method
        return self._hp   # we can not set value your self

    @property
    def name(self):
        return self._name

    def take_damage(self,damage):
        self._hp -= damage                   # _hp is class attribute
        self._hp = 0 if self._hp < 0 else self._hp

    @property
    def is_alive(self):
        return self._hp!=0

    @property
    def is_wounded(self):
        return self._hp <self._max_hp if self._hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive

bil = Character("Bil Farmer",100)
print(bil._hp)
print(bil.is_alive)
print(bil.is_wounded)
bil.take_damage(50)
print(bil.is_wounded)
print(bil.is_alive)
print(bil.is_dead)
bil.take_damage(50)
print(bil.is_wounded)
print(bil.is_dead)
