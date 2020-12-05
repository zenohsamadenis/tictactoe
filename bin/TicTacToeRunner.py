import numpy as np


# enum has to added
class Game:
    class _Cell:
        players = ["x", "o", ""]

        def __init__(self):
            self.used = False
            self.owner = self.players[3]

        def play(self, owner):
            try:
                if type(owner) != str:
                    raise TypeError("input was not a string. Try again!")
                if owner not in self.players:
                    raise ValueError(owner + "is not a player!")

            except TypeError:
                print(TypeError)
            except ValueError:
                print(ValueError)

            else:
                self.used = True
                self.owner = owner

    def __init__(self, size=3):
        self.Board = np.zeros((size, size)) * self._Cell()

    def turn(self, row, column):
        # not implemented yet
        pass
