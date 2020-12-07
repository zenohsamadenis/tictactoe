import numpy as np
import os


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
        print(p, end="")


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
            print("well done")
            return True

    def legal_input(self, player):
        allowed = ["1", "2", "3"]
        self.print()
        print()
        row = input(str(player.player_name) + ", select a row:")
        column = input(str(player.player_name) + ", select a column:")

        if row not in allowed or column not in allowed:
            print("Input is Wrong")
            return -1, -1
        else:
            return int(row)-1, int(column)-1

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
                print("|", end="")
                self.Board[i, j].print()
            print("|")
            print("_ _ _ _ _ _ _")


os.system("clear")

new_game = Game()
name_x = input("player1, type in your Name")
name_o = input("player2, type in your Name")

player_x = Player(player_name=name_x, sign="x")
player_o = Player(player_name=name_o, sign="o")

end_of_game = False
turn_player = player_o
# game_cont = True

while True:
    print("welcome to TicTacToe!")
    while not end_of_game:

        if turn_player == player_x:
            turn_player = player_o
        else:
            turn_player = player_x

        correct_input = False
        while not correct_input:
            row, column = new_game.legal_input(turn_player)
            os.system("clear")
            if row != -1:
                correct_input = new_game.turn(row, column, turn_player)
            else:
                print(str(turn_player.player_name) + ", try again")
        end_of_game = new_game.check(turn_player)

    print("congratulation, " + str(turn_player.player_name) + " you have won the game.")
    correct_input = False
    selection = None
    while not correct_input:
        selection = input("want to play a new game? (y|n)")
        if selection.upper() == "Y" or selection.upper() == "N":
            correct_input = True
    if selection.upper() == "N":
        break
    else:
        new_game = Game()
        player_x = Player(player_name=name_x, sign="x")
        player_o = Player(player_name=name_o, sign="o")
        end_of_game = False
        turn_player = player_x
