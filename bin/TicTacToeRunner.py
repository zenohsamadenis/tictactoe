import numpy as np
import os
from sys import platform


def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")


def return_input(allowed_values, game, message=""):
    while True:
        print(message)
        i = input()
        for a in allowed_values:
            if i.upper == a.upper:
                return i
        clear()
        print("bad input, try again")
        game.print()



class Player:
    def __init__(self, sign, player_name=""):
        self.player_name = player_name
        self.sign = sign


class Cell:
    def __init__(self):
        self.owner = None

    def play(self, owner):
        self.owner = owner

    def is_owner(self, player):
        if self.has_owner():
            return self.owner is player
        else:
            return False

    def has_owner(self):
        return self.owner is not None

    def print(self):
        if self.has_owner():
            p = " " + self.owner.sign + " "
        else:
            p = "   "
        print("|" + p, end="")


class Game:
    def __init__(self, size=3):
        self.Board = np.array([[Cell() for a in range(size)] for b in range(size)])
        self.size = size

    def turn(self, row, column, player):
        if self.Board[row, column].has_owner():
            print("This field is used")
            return False
        else:
            self.Board[row, column].play(player)
            print("good choice")
            return True

    def check(self, player):
        for row in range(3):
            game_over = True
            for column in range(3):
                if not self.Board[row, column].is_owner(player):
                    game_over = False
            if game_over:
                return True

        for column in range(3):
            game_over = True
            for row in range(3):
                if not self.Board[row, column].is_owner(player):
                    game_over = False
            if game_over:
                return True

        game_over = True
        for num in range(3):
            if not self.Board[num, num].is_owner(player):
                game_over = False
        if game_over:
            return True

        game_over = True
        for num in range(3):
            if not self.Board[num, -num].is_owner(player):
                game_over = False
        if game_over:
            return True

    def print(self):
        print("- - - - - - -")
        for i in range(3):
            for j in range(3):
                self.Board[i, j].print()
            print("|")
            print("_ _ _ _ _ _ _")


clear()
name_x = input("player1, type in your Name")
name_o = input("player2, type in your Name")
# game_cont = True

while True:
    clear()
    print("welcome to TicTacToe!")
    new_game = Game()
    player_x = Player(player_name=name_x, sign="x")
    player_o = Player(player_name=name_o, sign="o")
    end_of_game = False
    turn_player = player_o
    while not end_of_game:

        if turn_player == player_x:
            turn_player = player_o
        else:
            turn_player = player_x

        correct_input = False
        while not correct_input:
            new_game.print()
            allowed = ["1", "2", "3"]
            row = int(return_input(allowed, new_game, str(turn_player.player_name) + ", select a row:")) - 1
            column = int(return_input(allowed, new_game, str(turn_player.player_name) + ", select a column:")) - 1
            clear()
            correct_input = new_game.turn(row, column, turn_player)
        end_of_game = new_game.check(turn_player)
    new_game.print()
    print("congratulation, " + str(turn_player.player_name) + " you have won the game.")
    allowed = ["y", "n"]
    selection = return_input(["y", "n"], new_game, "want to play a new game? (y|n)")
    if selection.upper() == "N":
        print("No :( Im sad now!")
        break
