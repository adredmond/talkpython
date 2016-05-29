import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level

    def __repr__(self):
        return 'A {} of level {}'.format(self.name, self.level)


class Wizard(Creature):
    def attack(self, creature):
        attack_roll = self.get_defensive_roll()
        defense_roll = creature.get_defensive_roll()
        print('The hero rolls: ', attack_roll)
        print('The {} rolls: {}'.format(creature.name, defense_roll))
        if attack_roll > defense_roll:
            return True
        else:
            return False


class SmallAnimal(Creature):
    def __init__(self, *pargs):
        super().__init__(*pargs)

    def get_defensive_roll(self):
        return super().get_defensive_roll() / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire: bool):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_mod = 1.5 if self.breaths_fire else 1
        scale_mod = 1 + (self.scaliness * 0.01)
        return base_roll * fire_mod * scale_mod

    def __repr__(self):
        base = 'A {} of level {} with a scaliness of {}'.format(self.name, self.level, self.scaliness)
        if self.breaths_fire:
            return base + ', who breathes fire!'
        else:
            return base

