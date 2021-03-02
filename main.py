# CHESS
# 30 January 2021
# Matthew Coombe, Nurayn Hashim

import pygame
import pygame_gui
from pawn import Pawn
from queen import Queen
from bishop import Bishop
from rook import Rook
from king import King
from knight import Knight

pygame.init()
clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Chess")
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 0, 0))
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
image = pygame.image.load(r"C:\Users\\coomb\Documents\Python Problems\Chess\board.png")
image = pygame.transform.scale(image, (400, 400))
rect = image.get_rect()


board = [[None for i in range(8)] for j in range(8)]

for i in range(len(board[6])):
    p = Pawn((6, i), "black", "P")
    board[6][i] = p

# White pieces

board[0][0] = Rook((0, 0), "white", "R")
board[0][1] = Knight((0, 1), "white", "N")
board[0][2] = Bishop((0, 2), "white", "B")
board[0][3] = King((0, 3), "white", "K")
board[0][4] = Queen((0, 4), "white", "Q")
board[0][5] = Bishop((0, 5), "white", "B")
board[0][6] = Knight((0, 6), "white", "N")
board[0][7] = Rook((0, 7), "white", "R")

for i in range(len(board[1])):
    p = Pawn((1, i), "white", "P")
    board[1][i] = p

# Black pieces

board[7][0] = Rook((7, 0), "black", "R")
board[7][1] = Knight((7, 1), "black", "N")
board[7][2] = Bishop((7, 2), "black", "B")
board[7][3] = King((7, 3), "black", "K")
board[7][4] = Queen((7, 4), "black", "Q")
board[7][5] = Bishop((7, 5), "black", "B")
board[7][6] = Knight((7, 6), "black", "N")
board[7][7] = Rook((7, 7), "black", "R")

for i in range(len(board[1])):
    p = Pawn((6, i), "black", "P")
    board[6][i] = p


def printBoard():
    print("---------------------------------")
    for i in range(8):
        print("|", end="")
        for j in range(8):
            if board[i][j] is None:
                print(" 0 " + "|", end="")
            else:
                print(" " + board[i][j].getID() + " " + "|", end="")
        print("\n---------------------------------")


def main():
    print("Welcome")
    printBoard()
    moveInput = ""

    # for x in range(8):
    #     for y in range(8):
    #         if board[x][y] is not None and board[x][y].possibleMoves(board):
    #             print(board[x][y].getColour(), "", board[x][y].getID(), ": ", board[x][y].possibleMoves(board))

    # while not moveInput == "quit":
    #     moveInput = input("Enter move or \"quit\" to quit: ")
    #     move = moveInput.split()
    #
    #     try:
    #         goal = move[2]
    #         start = move[0]
    #         goalxy = (ord(goal[0]) - 97, int(goal[1]) - 1)
    #         startxy = (ord(start[0]) - 97, int(start[1]) - 1)
    #         print(startxy, "to", goalxy)
    #         if board[startxy[0]][startxy[1]] is None:
    #             print("No piece on square " + start)
    #         else:
    #             print(board[startxy[0]][startxy[1]].possibleMoves(board))
    #             if goalxy in board[startxy[0]][startxy[1]].possibleMoves(board):
    #                 temp = board[startxy[0]][startxy[1]]
    #                 board[startxy[0]][startxy[1]] = None
    #                 board[goalxy[0]][goalxy[1]] = temp
    #                 board[goalxy[0]][goalxy[1]].updatePosition(goalxy)
    #                 print(board[goalxy[0]][goalxy[1]].getPosition())
    #
    #             else:
    #                 print("Move not possible")
    #     except IOError as e:
    #         print("wrong input")
    #         continue

    # printBoard()
    while True:
        screen.fill((0, 0, 0))
        screen.blit(image, rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


if __name__ == '__main__':
    main()
