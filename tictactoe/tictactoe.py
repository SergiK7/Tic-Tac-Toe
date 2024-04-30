"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #if board == initial_state():
    #    return "X"

    count_X = 0
    count_O = 0

    for i in board:
        for j in i:
            if j == "X":
                count_X += 1
            elif j == "O":
                count_O += 1

    if count_X <= count_O:
        return "X"
    else:
        return "O"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError

    new_board = copy.deepcopy(board)

    move = player(new_board)

    new_board[action[0]][action[1]] = move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check if the winner has won horizontally
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] != None:
            return row[0]

    #Check if the winner has won vertically
    for i in range(3):
        column = []
        for j in range(3):
            column.append(board[j][i])
        if column[0] != None and len(set(column)) == 1:
            return column[0]

    #Check diagonally
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != None:
        return board[2][0]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0

def minimax_value(board):
    """
    Returns the minimax value of the board
    """

    if terminal(board):
        return utility(board)

    if player(board) == "X":
        value = -100
        for action in actions(board):
            value = max(value, minimax_value(result(board, action)))
        return value

    if player(board) == "O":
        value = 100
        for action in actions(board):
            value = min(value, minimax_value(result(board, action)))
        return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == "X":
        best_action = None
        best_value = -100

        for action in actions(board):
            value = minimax_value(result(board, action))
            if value > best_value:
                best_action = action
                best_value = value
        return best_action

    if player(board) == "O":
        best_action = None
        best_value = 100

        for action in actions(board):
            value = minimax_value(result(board, action))
            if value < best_value:
                best_action = action
                best_value = value
        return best_action
