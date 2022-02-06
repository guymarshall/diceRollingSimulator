import random


def roll_die(number_of_sides):
    return random.randint(1, number_of_sides)


def main():
    number_of_dice = int(input("Number of dice to roll: "))
    number_of_sides = int(input("Number of sides per die: "))

    for i in range(number_of_dice):
        print(roll_die(number_of_sides))


if __name__ == '__main__':
    main()
