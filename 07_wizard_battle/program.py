import random
import time

from actors import SmallAnimal, Creature, Wizard, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------------------')
    print('        WIZARD BATTLE')
    print('------------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        SmallAnimal('Bat', 3),
        Creature('Tiger', 12),
        Dragon('Dragon', 50, 25, True),
        Wizard('Evil Wizard', 100)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} appears out of a dark and foggy forest'.format(
            active_creature.name, active_creature.level))
        cmd = input('Do you [l]ook around, [a]ttack, or [r]unaway?').lower()
        if cmd == 'l':
            print('As the hero looks around, he sees: ')
            for c in creatures:
                print(' * ', c)
            print()
        elif cmd == 'a':
            if hero.attack(active_creature):
                print('The hero has triumphed over the nasty {}'.format(active_creature.name))
                creatures.remove(active_creature)
            else:
                print('The hero has been defeated and needs time to recover')
                time.sleep(5)
        elif cmd == 'r':
            print("The hero's confidence waivers, and he flees")
        else:
            print('okay, exiting game ... goodbye!')
            break

        if not creatures:
            print('you have defeated all of the monsters!')
            break

if __name__ == '__main__':
    main()
