"""
DaveBot - A deterministic bot who likes marriages
"""

# Will check for royal marriages first thing
# Will try to play lowest trump suit if opponents card isn't of trump suit and is a 10 or Ace
# Will attempt to play higher versions of same suit if lost previous trick
# Will attempt to play highest cards be default, but will avoid playing king or queen if possible

# Import the API objects
from api import State, Deck
import random


class Bot:

    def __init__(self):
        pass

    def check_royal_marriage(self, state, moves):
        possible_marriages = Deck.get_possible_mariages(state._deck, self)
        print("Dave's possible marriages: ")
        print(possible_marriages)
        print("\n")


    def get_move(self, state):
        # type: (State) -> tuple[int, int]

        # All legal moves
        moves = state.moves()

        self.check_royal_marriage(state, moves)

        print("Dave's available moves: \n")
        print(moves)
        print("\n")

        # Return a random choice
        return random.choice(moves)