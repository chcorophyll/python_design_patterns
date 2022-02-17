"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""


class LazyProperty(object):

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print("function overriden: {}".format(self.method))
        print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value


class Test(object):

    def __init__(self):
        self.x = "foo"
        self.y = "bar"
        self._resource = None

    @LazyProperty
    def resource(self):
        print("initializing self._resource which is: {}".format(self._resource))
        self._resource = tuple(range(5))
        return self._resource


# def main():
#     t = Test()
#     print(t.x)
#     print(t.y)
#     print(t.resource)
#     print(t.resource)


class SensitiveInfo(object):

    def __init__(self):
        self.users = ["nick", "tom", "ben", "mike"]

    def read(self):
        print("There are {} users: {}".format(len(self.users), " ".join(self.users)))

    def add(self, user):
        self.users.append(user)
        print("Added user {}".format(user))


class Info(object):

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = "0xdeadbeef"

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input("what is the secret? ")
        self.protected.add(user) if sec == self.secret else print("That is wrong!")


def main():
    info = Info()
    while True:
        print("1. read list |==| 2. add user |==| 3. quit")
        key = input("choose option: ")
        if key == "1":
            info.read()
        elif key == "2":
            name = input("choose username: ")
            info.add(name)
        elif key == "3":
            exit()
        else:
            print("unknown option: {}".format(key))


if __name__ == "__main__":
    main()