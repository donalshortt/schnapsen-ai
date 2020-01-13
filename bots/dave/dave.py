"""
DaveBot - A deterministic bot who likes marriages
"""

# Will check for marriages first thing
# Will try to play lowest trump suit if opponents card isn't of trump suit and is a 10 or Ace
# Will attempt to play higher versions of same suit if lost previous trick
# Will attempt to play highest cards be default, but will avoid playing king or queen if possible

# Import the API objects
from api import State, Deck
import random

class Bot:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def check_marriage(self, state, moves):
        possible_marriages = []
        for index in moves:
            if index[0] is not None and index[1] is not None:
                possible_marriages.append(index)

        # Check for royal marriages
        if possible_marriages:
            possible_royal_marriages = []
            for index in possible_marriages:
                if Deck.get_suit(index[0]) == state.get_trump_suit():
                    possible_royal_marriages.append(index)
                    return possible_royal_marriages

        return possible_marriages

    def get_move(self, state):
        me = state.whose_turn()
        moves = state.moves()

        # if marriage available and dave is leading
        possible_marriages = self.check_marriage(state, moves)
        if possible_marriages and state.get_opponents_played_card() is None:
            return possible_marriages[0]

        # Return a random choice
        return random.choice(moves)