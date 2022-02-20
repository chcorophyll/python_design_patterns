"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""

import os


verbose = True


class RenameFile(object):

    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile(object):

    def __init__(self, path, txt="Hello world!\n"):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode="w", encoding="utf-8") as file:
            file.write(self.txt)
    def undo(self):
        delete_file(self.path)


class ReadFile(object):

    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode="r", encoding="utf-8") as file:
            print(file.read(), end="")


def delete_file(path):
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    orig_name, new_name = "file_0", "file_1"

    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
    [c.execute() for c in commands]

    answer = input("reverse the executed commands? [y/n]")
    if answer not in "yY":
        print("the result is {}".format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


def main_2():
    orig_name = "file_0"
    df = delete_file
    commands = []
    # for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
    #     commands.append(cmd)
    commands.append(df)

    for c in commands:
        try:
            c.execute()
        except AttributeError as e:
            df(orig_name)

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == "__main__":
    main()