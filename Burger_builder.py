
from enum import Enum
import time

BurgerProgress = Enum('BurgerProgress', 'queue preparation cooking ready')
BurgerPatty = Enum('BurgerPatty', 'beef chicken')
BurgerBun = Enum('BurgerBun', 'sesame plain')
BurgerTopping = Enum('BurgerTopping', 'lettuce tomato cheese pickles onions')
STEP_DELAY = 3


class Burger:
    def __init__(self, name):
        self.name = name
        self.patty = None
        self.bun = None
        self.toppings = []

    def __str__(self):
        return self.name

    def prepare_patty(self, patty):
        self.patty = patty
        print(f'Preparing the {self.patty.name} patty for your {self}')
        time.sleep(STEP_DELAY)
        print(f'Done preparing the {self.patty.name} patty')

    def prepare_bun(self, bun):
        self.bun = bun
        print(f'Preparing the {self.bun.name} bun for your {self}')
        time.sleep(STEP_DELAY)
        print(f'Done preparing the {self.bun.name} bun')

    def add_toppings(self, *toppings):
        print(f'Adding toppings to your {self}: {", ".join(t.name for t in toppings)}')
        self.toppings.extend(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done adding toppings to your {self}')


class BeefBurgerBuilder:
    def __init__(self):
        self.burger = Burger('Beef Burger')
        self.progress = BurgerProgress.queue
        self.cooking_time = 10

    def prepare_patty(self):
        self.progress = BurgerProgress.preparation
        self.burger.prepare_patty(BurgerPatty.beef)

    def prepare_bun(self):
        self.progress = BurgerProgress.preparation
        self.burger.prepare_bun(BurgerBun.sesame)

    def add_toppings(self):
        topping_items = (
            BurgerTopping.lettuce,
            BurgerTopping.tomato,
            BurgerTopping.cheese,
            BurgerTopping.pickles,
            BurgerTopping.onions
        )
        self.burger.add_toppings(*topping_items)

    def cook(self):
        self.progress = BurgerProgress.cooking
        print(f'Cooking your beef burger for {self.cooking_time} seconds')
        time.sleep(self.cooking_time)
        self.progress = BurgerProgress.ready
        print('Your beef burger is ready!')


class ChickenBurgerBuilder:
    def __init__(self):
        self.burger = Burger('Chicken Burger')
        self.progress = BurgerProgress.queue
        self.cooking_time = 8

    def prepare_patty(self):
        self.progress = BurgerProgress.preparation
        self.burger.prepare_patty(BurgerPatty.chicken)

    def prepare_bun(self):
        self.progress = BurgerProgress.preparation
        self.burger.prepare_bun(BurgerBun.plain)

    def add_toppings(self):
        topping_items = (
            BurgerTopping.lettuce,
            BurgerTopping.tomato,
            BurgerTopping.pickles,
            BurgerTopping.onions
        )
        self.burger.add_toppings(*topping_items)

    def cook(self):
        self.progress = BurgerProgress.cooking
        print(f'Cooking your chicken burger for {self.cooking_time} seconds')
        time.sleep(self.cooking_time)
        self.progress = BurgerProgress.ready
        print('Your chicken burger is ready!')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_burger(self, builder):
        self.builder = builder
        steps = (builder.prepare_patty, builder.prepare_bun, builder.add_toppings, builder.cook)
        [step() for step in steps]

    @property
    def burger(self):
        return self.builder.burger


def validate_type(builders):
    try:
        input_msg = 'What burger would you like, [b]eef or [c]hicken? '
        burger_type = input(input_msg)
        builder = builders[burger_type]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only beef (key b) and chicken (key c) burgers are available.'
        print(error_msg)
        valid_input = False
        builder = None
    return valid_input, builder


def main():
    builders = {'b': BeefBurgerBuilder, 'c': ChickenBurgerBuilder}
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_type(builders)
    print("\n")
    waiter = Waiter()
    waiter.construct_burger(builder)
    burger = waiter.burger
    print("\n")
    print(f'Enjoy your {burger}!')


if __name__ == '__main__':
    main()
