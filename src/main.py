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
                    print(colored("Black is in Check!", "green"))
                elif board.turn == True:
                    print(colored("White is in Check!", "green"))
            else:
               print(colored("That move is Legal", "green"))
        else:
            if playerMove in str(board.pseudo_legal_moves).lower():
                print(colored("You are in Check, or Pinned. That move is Illegal", "red"))
                loss()
            else:
                print(colored("That move is Illegal", "red"))
                loss()

    def tie():
        print("It is no longer possible to Checkmate. The game is henceforth a Draw...")
        newGame = input("Play Again? (y,n): ")
        if newGame == "y":
            board.clear_stack()
            chessGame()
        elif newGame == "n":
            sys.exit()
    
    print("")