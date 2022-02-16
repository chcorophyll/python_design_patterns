"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""


quotes = ("A man is not complete until he is married. Then he is finished.",
          "As I said before, I never repeat myself.",
          "Behind a successful man is an exhausted woman.",
          "Black holes really suck...",
          "Facts are stubborn things.")


class QuoteModel(object):

    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as e:
            value = "Not Found!"
        return value


class QuoteTerminalView(object):

    def show(self, quote):
        print("And the quote is: '{}'".format(quote))

    def error(self, msg):
        print("Error: {}".format(msg))

    def select_quote(self):
        return input("Which quote number would you like to see?")


class QuoteTerminalController(object):

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError as e:
                self.view.error("Incorrect index '{}".format(n))
            else:
                valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == "__main__":
    main()