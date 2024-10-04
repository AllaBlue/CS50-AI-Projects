"""
Tic Tac Toe Player
"""

import math
import copy

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

    # Count how many Xs, Os and empty cells there are in the board
    countX = 0
    countO = 0
    countEmpty = 0

    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
            else:
                countEmpty += 1

    # If all cells are empty, then it is X player turn, 
    # if number of Xs cells is bigger than number of Os cells then it is O player turn, 
    # otherwise X player turn      
    if countEmpty == 9:
        return X
    elif countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    (i, j) = action

    if new_board[i][j] != EMPTY:
        raise Exception("Action is not valid")
    elif i < 0 or i > len(board[0]) or j < 0 or j > len(board[0]):
        raise IndexError("Out of bounds move")
    else:
        if player(board) == X:
            new_board[i][j] = X
        elif player(board) == O:
            new_board[i][j] = O
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    count = 0
    winner_rows = []
    winner_columns = []
    winner_diagonal_1 = []
    winner_diagonal_2 = []

    while count < len(board[0]):
        for i, row in enumerate(board):
            for j, cell in enumerate(board):
                
                if i == count:
                    winner_rows.append(board[i][j])
                
                if j == count:
                    winner_columns.append(board[i][j])

                if i == j: 
                    winner_diagonal_1.append(board[i][j])

                if i+j == 2:
                    winner_diagonal_2.append(board[i][j])
        
        # Check if there is a winner in rows
        if all(cell == X for cell in winner_rows):
            return X
        elif all(cell == O for cell in winner_rows):
            return O
        
        # Check if there is a winner in columns
        if all(cell == X for cell in winner_columns):
            return X
        elif all(cell == O for cell in winner_columns):
            return O
        
        # Check if there is a winner in diagonal_1 (\)
        if all(cell == X for cell in winner_diagonal_1):
            return X
        elif all(cell == O for cell in winner_diagonal_1):
            return O
        
        # Check if there is a winner in diagonal_2 (/)
        if all(cell == X for cell in winner_diagonal_2):
            return X
        elif all(cell == O for cell in winner_diagonal_2):
            return O

        count += 1
        winner_rows = []
        winner_columns = []
        winner_diagonal_1 = []
        winner_diagonal_2 = []
    
    return None

                
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    w = winner(board)

    # If there is a winner, game is over
    if w == X:
        return True
    elif w == O:
        return True

    # Check how many empty cells in the board.
    # If there is at least one empty cell, game is not over
    # If there are no empty cells in the board, game is over
    empty_count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_count += 1
                return False
    
    if empty_count == 0:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    p = player(board)

    # If player is X  - it is maximum player
    if p == X:
        # res is am array [value, optimal_action], 
        # where value is -1, 1, or 0 and optimal action is a tupple with coordinates of the optimal action for the player
        res = max_value(board)
        
        # if res contains both value and optimal_action, function returns optimal_action, 
        # because game is not over yet. Otherwise, if res contains only one elemnt,
        # game is already over so function returns None
        if len(res) > 1:
            return res[1]
        else:
            return None 
    # If player is O  - it is minimum player 
    elif p == O:
        res = min_value(board)

        if len(res) > 1:
            return res[1]
        else:
            return None


def max_value(board):
    v = -math.inf
    # k - is a value that keeps track of when v is changed.
    k = v
    optimal_max_action = ()

    if terminal(board):
        return [utility(board)]

    for action in actions(board):
        v = max(v, min_value(result(board, action))[0])
        # when v is changed we change optimal_action too
        if v != k:
            k = v
            optimal_max_action = action
    
    return [v, optimal_max_action]


def min_value(board):
    v = math.inf
    # k - is a value that keeps track of when v is changed.
    k = v
    optimal_min_action = ()

    if terminal(board):
        return [utility(board)]

    for action in actions(board):
        v = min(v, max_value(result(board, action))[0])
        # when v is changed we change optimal_action too
        if v != k:
            k = v
            optimal_min_action = action
    
    # print(f"optimal_min_action - {optimal_min_action}")
    return [v, optimal_min_action]
