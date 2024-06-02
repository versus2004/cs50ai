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
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if(col == X):
                x_count += 1
            elif(col == O):
                o_count += 1
    current_turn = X
    if(x_count>o_count):
        current_turn = O
    return current_turn


def actions(board):
    possible = set()
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j]==EMPTY:
                possible.add((i,j))
    return possible
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):

    currplayer=player(board)

    boardcopy=copy.deepcopy(board)
    i,j=action
    if board[i][j]!=EMPTY:
        raise Exception
    else:
        boardcopy[i][j]=currplayer
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return boardcopy
    raise NotImplementedError


def winner(board):
    players=(X,O)
    for player in players:

        #check rows
        for row in board:
            if row==[player,player,player]:
                return player
           
         # Check columns
        for col in range(3):
            column = [row[col] for row in board] 
            if all(cell == player for cell in column):
                return player
        #check both the diagonals
        if all(board[i][i] == player for i in range(3)):
            return player

        # Top-right to bottom-left diagonal
        if all(board[i][2 - i] == player for i in range(3)):
            return player

    """
    Returns the winner of the game, if there is one.
    """
    return None
    raise NotImplementedError
print(winner(initial_state()))
def terminal(board):
    if winner(board)!=None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    raise NotImplementedError



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimalmove = ()
        if terminal(board):
            return utility(board),optimalmove
        else:
            v = -math.inf
            for action in actions(board):
                minvalue = min_value(result(board, action))[0]
                if minvalue > v:
                    v = minvalue
                    optimalmove = action
            return v, optimalmove

    def min_value(board):
        optimalmove = ()
        if terminal(board):
            return utility(board),optimalmove
        else:
            v = math.inf
            for action in actions(board):
                maxvalue = max_value(result(board, action))[0]
                if maxvalue < v:
                    v = maxvalue
                    optimalmove = action
            return v, optimalmove

    currplayer = player(board)

    if terminal(board):
        return None

    if currplayer == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]