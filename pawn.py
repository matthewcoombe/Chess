from piece import Piece
from typing import List, Tuple


class Pawn(Piece):

    def __init__(self, position: tuple, colour: str, pieceID: str):
        super().__init__(position, colour, pieceID)
        self.counter = 0

    def possibleMoves(self, grid):
        moves = []
        if self.colour == "white":
            if grid[self.x + 1][self.y] is None:
                moves.append((self.x + 1, self.y))
                if self.counter == 0 and grid[self.x + 2][self.y] is None:
                    moves.append((self.x + 2, self.y))
            if self.inRange(self.x + 1, self.y + 1) and grid[self.x + 1][self.y + 1] is not None and grid[self.x + 1][self.y + 1].getColour() == "black":
                moves.append((self.x + 1, self.y + 1))
            if self.inRange(self.x + 1, self.y - 1) and grid[self.x + 1][self.y - 1] is not None and grid[self.x + 1][self.y - 1].getColour() == "black":
                moves.append((self.x + 1, self.y - 1))
        elif self.colour == "black":
            if grid[self.x - 1][self.y] is None:
                moves.append((self.x - 1, self.y))
                if self.counter == 0 and grid[self.x - 2][self.y] is None:
                    moves.append((self.x - 2, self.y))
            if self.inRange(self.x - 1, self.y + 1) and grid[self.x - 1][self.y + 1] is not None and grid[self.x - 1][self.y + 1].getColour() == "white":
                moves.append((self.x - 1, self.y + 1))
            if self.inRange(self.x - 1, self.y - 1) and grid[self.x - 1][self.y - 1] is not None and grid[self.x - 1][self.y - 1].getColour() == "white":
                moves.append((self.x - 1, self.y - 1))
        return moves
