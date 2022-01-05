import chess
from termcolor import colored
import sys

isLegal = True
board = chess.Board()

def loss():
    global board
    if board.turn == True:
        print(colored("White Lost", "red"))
    else:
        print(colored("Black Lost", "red"))

    newGame = input("Play Again? (y/n): ")
    if newGame == "y":
        board.clearStack()
        chessGame()
    elif newGame == "n":
        sys.exit()

def chessGame():
    global board

    def move(board):
        if board.turn == True:
            print(colored(str(board), attrs=["bold"]))
            playerMove = input("White to Move: ")
        elif board.turn == False:
            print(colored(str(board)[::-1], attrs=["bold"]))
            playerMove = input("Black to Move: ")
        if playerMove.lower() == "resign":
            loss()
        legalMoves(playerMove)
        board = board.push_san(playerMove)
        return board
    
    def legalMoves(playerMove):
        playerMove = str(playerMove).lower()
        if playerMove in str(board.legal_moves).lower():
            if board.is_check():
                if board.turn == False:
                    print(colored(board))