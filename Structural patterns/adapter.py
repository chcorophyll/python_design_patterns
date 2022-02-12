"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""
class Synthesizer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} the synthesizer".format(self.name)

    def play(self):
        return "is playing an electronic song"


class Human(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} the human".format(self.name)

    def speak(self):
        return "say hello"


class Computer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} the computer".format(self.name)

    def execute(self):
        return "executes a program"


class Adapter(object):

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer("Apple")]
    synth = Synthesizer("Moog")
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human("Jack")
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print("{} {}".format(str(i), i.execute()))


if __name__ == "__main__":
    main()