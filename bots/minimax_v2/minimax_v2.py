#!/usr/bin/env python
"""


"""

from api import State, util
import random

class Bot:

    __max_depth = -1
    __randomize = True

    def __init__(self, randomize=True, depth=6):
        """
        :param randomize: Whether to select randomly from moves of equal value (or to select the first always)
        :param depth:
        """
        self.__randomize = randomize
        self.__max_depth = depth

    def get_move(self, state):
        # type: (State) -> tuple[int, int]

        val, move = self.value(state)

        return move

    def value(self, state, depth = 0, leadcount = -3):
        """
        Return the value of this state and the associated move
        :param state:
        :param depth:
        :return: A tuple containing the value of this state, and the best move for the player currently to move
        """

        if state.finished():
            winner, points = state.winner()
            return (points, None) if winner == 1 else (-points, None)

        if depth == self.__max_depth:
            return heuristic(state, leadcount)

        moves = state.moves()

        if self.__randomize:
            random.shuffle(moves)

        best_value = float('-inf') if maximizing(state) else float('inf')
        best_move = None

        for move in moves:

            next_state = state.next(move)

            if is_player_leading_trick(next_state):
                leadcount = leadcount + 1

            value, m = self.value(next_state, depth + 1, leadcount)

            if maximizing(state):
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_value, best_move

def maximizing(state):
    # type: (State) -> bool
    """
    Whether we're the maximizing player (1) or the minimizing player (2).

    :param state:
    :return:
    """
    return state.whose_turn() == 1

def is_player_leading_trick(state):
    # determines whether or not the player is leading the trick for the given state
    if state.leader() == state.whose_turn():
        return True
    else:
        return False

def heuristic(state, leadcount):
    # type: (State, int) -> float
    """
    Estimate the value of this state: -1.0 is a certain win for player 2, 1.0 is a certain win for player 1
    :param state:
    :return: A heuristic evaluation for the given state (between -1.0 and 1.0)
    """

    leadcount_heuristic = leadcount / 10
    ratio_heuristic = util.ratio_points(state, 1) * 2.0 - 1.0

    if

    evaluation = leadcount_heuristic + ratio_heuristic

    return evaluation, None