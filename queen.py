from piece import Piece
from typing import List, Tuple


class Queen(Piece):

    def __init__(self, position: tuple, colour: str, pieceID: str):
        super().__init__(position, colour, pieceID)
        self.counter = 0

    def possibleMoves(self, grid):
        moves = []
        # vertically
        i = 1
        while self.inRange(self.x + i, self.y) and (grid[self.x + i][self.y] is None or not grid[self.x + i][
                                                                                                self.y].getColour() == self.colour):
            moves.append((self.x + i, self.y))
            if grid[self.x + i][self.y] is not None and not grid[self.x + i][self.y].getColour() == self.colour:
                break
            i += 1
        i = 1
        while self.inRange(self.x - i, self.y) and (grid[self.x - i][self.y] is None or not grid[self.x - i][
                                                                                                self.y].getColour() == self.colour):
            moves.append((self.x - i, self.y))
            if grid[self.x - i][self.y] is not None and not grid[self.x - i][self.y].getColour() == self.colour:
                break
            i += 1
        # horizontally
        i = 1
        while self.inRange(self.x, self.y + i) and (grid[self.x][self.y + i] is None or not grid[self.x][
                                                                                                self.y + i].getColour() == self.colour):
            moves.append((self.x, self.y + i))
            if grid[self.x][self.y + i] is not None and not grid[self.x][self.y + i].getColour() == self.colour:
                break
            i += 1
        i = 1
        while self.inRange(self.x, self.y - i) and (grid[self.x][self.y - i] is None or not grid[self.x][
                                                                                                self.y - i].getColour() == self.colour):
            moves.append((self.x, self.y - i))
            if grid[self.x][self.y - i] is not None and not grid[self.x][self.y - i].getColour() == self.colour:
                break
            i += 1
        # diagonally
        i = 1
        while self.inRange(self.x + i, self.y + i) and (grid[self.x + i][self.y + i] is None or not grid[self.x + i][
                                                                                                        self.y + i].getColour() == self.colour):
            moves.append((self.x + i, self.y + i))
            if grid[self.x + i][self.y + i] is not None and not grid[self.x + i][self.y + i].getColour() == self.colour:
                break
            i += 1
        i = 1
        while self.inRange(self.x - i, self.y - i) and (grid[self.x - i][self.y - i] is None or not grid[self.x - i][
                                                                                                        self.y - i].getColour() == self.colour):
            moves.append((self.x - i, self.y - i))
            if grid[self.x - i][self.y - i] is not None and not grid[self.x - i][self.y - i].getColour() == self.colour:
                break
            i += 1
        i = 1
        while self.inRange(self.x + i, self.y - i) and (grid[self.x + i][self.y - i] is None or not grid[self.x + i][
                                                                                                        self.y - i].getColour() == self.colour):
            moves.append((self.x + i, self.y - i))
            if grid[self.x + i][self.y - i] is not None and not grid[self.x + i][self.y - i].getColour() == self.colour:
                break
            i += 1
        i = 1
        while self.inRange(self.x - i, self.y + i) and (grid[self.x - i][self.y + i] is None or not grid[self.x - i][
                                                                                                        self.y + i].getColour() == self.colour):
            moves.append((self.x - i, self.y + i))
            if grid[self.x - i][self.y + i] is not None and not grid[self.x - i][self.y + i].getColour() == self.colour:
                break
            i += 1

        return moves
