#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors,
lizard, spock between two Players,
and reports both Player's scores each round."""
# List of moves
moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):

        # To store the moves list it in an instance variable
        self.my_move = moves
        # To make the first round to have a random choice
        self.their_move = random.choice(moves)
    # The move method for player class...
    # ..this player will always play rock

    def move(self):
        return 'rock'

# To store moves of players
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    # Returns random choices from moves list
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    # This enable humans to play by returning humans' input
    def move(self, user_input):
        return user_input


class ReflectPlayer(Player):
    # This returns the last move of the human player
    # ..from the previous round
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    # This cycles through the moves
    # ..from the moves list
    def move(self):
        if self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        elif self.my_move == moves[2]:
            return moves[3]
        elif self.my_move == moves[3]:
            return moves[4]
        else:
            return moves[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        # Initialization of scores so we can keep track of them
        self.p1Score = 0
        self.p2Score = 0
        self.round = 0

    def play_round(self):
        # Getting user input
        user_input = input("Rock, paper, scissors, spock, lizard? > ").lower()
        # Handling invalid input
        if (("rock" in user_input and len(user_input) == 4) or
            ("paper" in user_input and len(user_input) == 5) or
            ("scissors" in user_input and len(user_input) == 8) or
            ("spock" in user_input and len(user_input) == 5) or
                ("lizard") in user_input and len(user_input) == 6):
            # If input is successful do all these at the bottom
            # 1 Call the move method from player 1 class
            move1 = self.p1.move(user_input)
            # 2 Call the move method from player 2 class
            move2 = self.p2.move()

            # To do this if player1 wins player2
            if self.beats(move1, move2):
                print(f"You played {move1}.")
                print(f"Opponent played {move2}.")
                print(f"{bcolors.OKGREEN}** PLAYER 1 "
                      f"WINS**{bcolors.ENDC}")
                self.p1Score += 1
                self.round += 1

            # To do this if they made same move
            elif move1 == move2:
                print(f"You played {move1}.")
                print(f"Opponent played {move2}.")
                print("** TIE **")
                self.round += 1
            else:
                # To do this If player 2 wins player 1
                print(f"You played {move1}.")
                print(f"Opponent played {move2}.")
                print(f"{bcolors.OKGREEN}** PLAYER "
                      f"2 WINS **{bcolors.OKGREEN}")
                self.p2Score += 1
                self.round += 1

            # To display score after every round
            print(f"{bcolors.WARNING}Score: Player One "
                  f"{self.p1Score}, Player "
                  f"Two {self.p2Score}.\n{bcolors.ENDC}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)

            # If user types "abandon"
        elif "abandon" in user_input:
            print(f"{bcolors.FAIL}You have "
                  f"abandoned the game.\n{bcolors.ENDC}"
                  "Goodbye!")
            exit()
        else:
            # To handle failed inputs
            self.play_round()

# This function sets the rules of the game
# and checks if one choice beats the other

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock') or
                (one == 'spock' and two == 'lizard') or
                (one == 'paper' and two == 'rock') or
                (one == 'rock' and two == 'lizard') or
                (one == 'lizard' and two == 'spock') or
                (one == 'spock' and two == 'scissors') or
                (one == 'scissors' and two == 'lizard') or
                (one == 'lizard' and two == 'paper') or
                (one == 'paper' and two == 'spock') or
                (one == 'spock' and two == 'rock') or
                (one == 'paper' and two == 'rock'))

# First function call when the game starts
    def play_game(self):
        print(f"Type {bcolors.BOLD}\"abandon\""
              f"{bcolors.ENDC} to abandon game, keep "
              "playing to play till the end.\n "
              "Let's play.\n")
        # A loop that increases the round
        while ((self.p1Score - self.p2Score < 3) or
               (self.p2Score - self.p1Score < 3)):
            print(f"{bcolors.OKBLUE}Round {self.round} --{bcolors.ENDC}")
            self.play_round()

            # This is called if one player is ahead of the other by 3
            if ((self.p1Score - self.p2Score == 3) or
                    (self.p2Score - self.p1Score == 3)):
                if self.p1Score > self.p2Score:
                    print("GAMEOVER!!\n Final "
                          "score:\n"
                          f"{bcolors.UNDERLINE}{bcolors.WARNING}Player 1 "
                          f"scored {self.p1Score} points "
                          f"and Player 2 scored "
                          f"{self.p2Score} points.\n"
                          f"{bcolors.ENDC}"
                          f"{bcolors.OKGREEN}Player "
                          f"1 is the overall Winner.\n"
                          f"{bcolors.ENDC}"
                          "Thanks for playing")
                    exit()
                elif self.p1Score == self.p2Score:
                    print("GAMEOVER!!\n Final score:\n"
                          f"Player 1 scored {self.p1Score} points "
                          f"and Player 2 scored {self.p2Score} point.s\n"
                          "It is a TIE.\n"
                          "Thanks for playing")
                    exit()
                else:
                    print("GAMEOVER!!\n Final score:\n"
                          f"{bcolors.UNDERLINE}Player 1 "
                          f"scored {self.p1Score} points "
                          f"and Player 2 scored {self.p2Score} "
                          f"points.\n{bcolors.ENDC}"
                          f"{bcolors.OKGREEN}Player 2 is the overall "
                          f"Winner.\n{bcolors.ENDC}"
                          f"Thanks for playing")
                    exit()
                break
                exit()


if __name__ == '__main__':
    # To add colors to texts
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    # First texts to be printed when game starts
    while True:
        print("ROCK, PAPER, SCISSORS, LIZARD, SPOCK - GO!\n")
        response = input("Choose an opponent: (1) Random "
                         "(2) Reflect (3) Repeat"
                         "(4) Cycle\n"
                         "Choose 1, 2, 3 or 4. "
                         f"Or type {bcolors.BOLD}\"quit\" "
                         f"{bcolors.ENDC} to exit the Game > ").lower()
        # Handling errors in input
        if (("1" in response and len(response) == 1) or
            ("2" in response and len(response) == 1) or
            ("3" in response and len(response) == 1) or
                ("4") in response and len(response) == 1):

            opponetList = [0, 1, 2, 3, 4, 5]
            # List of opponent Players (from 1 - 4) a user can choose from
            opponent = ['', RandomPlayer(),
                        ReflectPlayer(), Player(), CyclePlayer()]
            # converting string response to integer
            response_to_int = int(float(response))
            # Using user response to select an opponent player from the
            # opponent list
            if response_to_int in opponetList:
                game = Game(HumanPlayer(), opponent[response_to_int])
                game.play_game()
            else:
                print("Please choose properly")
        elif "quit" in response:
            print("Thanks for playing")
            exit()
        else:
            print(f"{bcolors.OKCYAN}Please choose an opponent{bcolors.ENDC}")

