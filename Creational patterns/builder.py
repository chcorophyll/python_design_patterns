"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""
from enum import Enum
import time


# factory method
MINI14 = "1.4GHz Mac mini"


class AppleFactory(object):

    class MacMini14(object):

        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = "Intel HD Graphics 5000"

        def __str__(self):
            info = ("Model: {}".format(MINI14),
                    "Memory: {}GB".format(self.memory),
                    "Hard Disk: {}GB".format(self.hdd),
                    "Graphics Card: {}".format(self.gpu))
            return "\n".join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print("I dont't know how to build {}".format(model))


# builder
class Computer(object):

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ("Model: {}".format(self.serial_number),
                "Memory: {}GB".format(self.memory),
                "Hard Disk: {}GB".format(self.hdd),
                "Graphics Card: {}".format(self.gpu))
        return "\n".join(info)


class ComputerBuilder(object):

    def __init__(self):
        self.computer = Computer("AG23385193")

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer(object):

    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=8, hdd=500, gpu="GeForce GTX 3090 Ti")
    computer = engineer.computer
    print(computer)


# pizza builder
PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")
STEP_DELAY = 3


class Pizza(object):

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print("preparing the {} dough of your {}...".format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print("done with the {} dough".format(self.dough.name))


class MargaritaBuilder(object):

    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding the tomato sauce to your margarita...")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        print("adding the topping (double mozzarella, oregano) to your margarita...")
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("done with the topping (double mozzarella, oregano)")

    def bake(self):
        self.progress = PizzaProgress.baking
        print("baking your margarita for {} seconds".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("your margarita is ready")


class CreamyBaconBuilder(object):

    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print("adding the crème fraîche sauce to your creamy bacon...")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print("done with the crème fraîche sauce")

    def add_topping(self):
        print("adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon...")
        self.pizza.topping.append([i for i in (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                               PizzaTopping.ham, PizzaTopping.mushrooms,
                                               PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)")

    def bake(self):
        self.progress = PizzaProgress.baking
        print("baking your creamy bacon for {} seconds".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("your creamy bacon is ready")


class Waiter(object):

    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input("What pizza would you like, [m]argarita or [c]reamy bacon?")
        builder = builders[pizza_style]()
        # valid_input = True
    except KeyError as e:
        print("Sorry, only margarita (key m) and creamy bacon (key c) are available")
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print("Enjoy your {}!".format(pizza))


# other builder
class Pizza(object):

    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = "yes" if self.garlic else "no"
        cheese = "yes" if self.extra_cheese else "no"
        info = ("Garlic: {}".format(garlic), "Extra cheese: {}".format(cheese))
        return "\n".join(info)

    class PizzaBuilder(object):

        def __init__(self):
            self.garlic = False
            self.extra_cheese = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)


if __name__ == "__main__":
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
    main()
    # pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
    # print(pizza)


