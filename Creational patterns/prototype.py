"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""
import copy
from collections import OrderedDict


class Book(object):

    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        my_list = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            my_list.append("{}: {}".format(i, ordered[i]))
            if i == "price":
                my_list.append("$")
            my_list.append("\n")
        return "".join(my_list)


class Prototype(object):

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrect object identifier: {}".format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    book_0 = Book("The C Programming Language",
                ("Brian W. Kernighan", "Dennis M.Ritchie"),
                price=118,
                publisher="Prentice Hall",
                length=228,
                publication_date="1978-02-22",
                tags=("C", "programming", "algorithms", "data structures"))
    prototype = Prototype()
    cid = "k&r-first"
    prototype.register(cid, book_0)
    book_1 = prototype.clone(cid,
                             name="The C Programming Language(ANSI)",
                             price=48.99,
                             length=274,
                             publication_date="1988-04-01",
                             edition=2)
    for b in (book_0, book_1):
        print(b)
    print("ID b1: {} != ID b2: {}".format(id(book_0), id(book_1)))


if __name__ == "__main__":
    main()
