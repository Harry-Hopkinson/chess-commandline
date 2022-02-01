import chess
from termcolor import colored
import sys

isLegal = True
board = chess.Board()
moveList = ""
round = 1
firstRun = True
diff = 0


def loss():
    global board
    if board.turn == True:
        print(colored("White has been Checkmated!", "red"))
        print(colored("White Lost", "red"))
    else:
        print(colored("Black has been Checkmated!", "red"))
        print(colored("Black Lost", "red"))

    newGame = input("Play Again? (y/n): ")
    if newGame == "y":
        board.clear_stack()
        chessGame()
    elif newGame == "n":
        print(colored("Thanks for playing!", "red"))
        print(colored("Exiting Program...", "red"))
        sys.exit()


def chessGame():
    global board
    global moveList
    global round

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
        global moveList
        global firstRun
        global round
        global diff

        playerMove = str(playerMove).lower()
        if playerMove in str(board.legal_moves).lower():
            if board.is_check():
                if board.turn == False:
                    print(colored("Black is in Check!", "green"))
                elif board.turn == True:
                    print(colored("White is in Check!", "green"))
            else:
                if round % 2 != 0:
                    if firstRun:
                        print(colored("That move is Legal", "green"))
                        moveList += str(round) + ": " + playerMove + " "
                        print(moveList)
                        firstRun = False
                    else:
                        print(colored("That move is Legal", "green"))
                        moveList += str(round - diff) + ": " + playerMove + " "
                        print(moveList)
                    round += 1
                    diff += 1
                else:
                    print(colored("That move is Legal", "green"))
                    moveList += " " + playerMove + " "
                    print(moveList)
                    round += 1
        else:
            if playerMove in str(board.pseudo_legal_moves).lower():
                print(
                    colored("You are in Check, or Pinned. That move is Illegal", "red"))
                print("Move again...", "red")
                move(board)
            else:
                print(colored("That move is Illegal", "red"))
                print("Move again...", "red")
                move(board)

    def tie():
        print("It is no longer possible to Checkmate. The game is henceforth a Draw...")
        newGame = input("Play Again? (y,n): ")
        if newGame == "y":
            board.clear_stack()
            chessGame()
        elif newGame == "n":
            print(colored("Thanks for playing!", "red"))
            print(colored("Exiting Program...", "red"))
            sys.exit()

    print('\033[2J')  # clears the console
    print(colored("Chess in the Console!", "blue"))
    print(colored("""Rules:
    1. Normal Chess rules apply
    2. You can only use algebraic notation (FIDE standard)
    3. Use the Algebraic Notation with a Starting Capital Letter for a major piece - if a minor piece use a lowercase character e.g Nxd4 or e4
    4. Try not to do illegal moves\n""", 'white'))

    while True:
        board = chess.Board(board.fen())
        move(board)
        if board.is_game_over():
            if board.is_checkmate():
                loss()
            elif board.is_stalemate() or board.is_insufficient_material():
                tie()


if chessGame() == "__main__":
    chessGame()
