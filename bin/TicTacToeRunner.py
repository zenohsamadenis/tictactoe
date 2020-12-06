import numpy as np


class _Cell:
    __players = ["x", "o", ""]

    def __init__(self):
        self.used = False
        self.owner = self.__players[2]

    def play(self, owner):
        self.used = True
        self.owner = owner


# enum has to added
class Game:
    def __init__(self, size=3):
        self.Board = np.zeros((size, size)) * _Cell()

    def turn(self, row, column, owner):
        try:
            if type(row) != int or type(column) != int:
                raise TypeError("")
            if self.Board(row, column).used:
                self.Board(row, column).play(owner)
            raise KeyError("Feld ist schon benutzt")
        except KeyError as e:
            print(e)


print("want to play a new game?")

new_game = Game()

