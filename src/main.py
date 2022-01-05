import chess
from termcolor import colored
import sys

is_legal = True
board = chess.Board()

def loss():
    global board

    if board.turn == True:
        print(colored("White Lost", "red"))
    else:
        print(colored("Black Lost", "red"))
