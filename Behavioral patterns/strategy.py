"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""
import time


SLOW = 3
LIMIT = 5
WARNING = "too bad, you picked the slow algorithm :("


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def all_unique_sort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    sorted_s = sorted(s)
    for c_0, c_1 in pairs(sorted_s):
        if c_0 == c_1:
            return False
    return True


def all_unique_set(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def all_unique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input("Insert word (type quit to exit)> ")
            if word == "quit":
                print("bye")
                return
            strategy_picked = None
            strategies = {'1': all_unique_set, '2': all_unique_sort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input("Choose strategy: [1] Use a set, [2] Sort and pair> ")
                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, all_unique(word, strategy)))
                except KeyError as e:
                    print("Incorrect option: {}".format(strategy_picked))
            print("**********************")


if __name__ == "__main__":
    main()


