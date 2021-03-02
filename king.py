from piece import Piece
from typing import List, Tuple


class King(Piece):

    def __init__(self, position: tuple, colour: str, pieceID: str):
        super().__init__(position, colour, pieceID)
        self.counter = 0

    def possibleMoves(self, grid):
        moves = []
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                if self.inRange(x, y) and (grid[x][y] is None or grid[x][y].getColour == self.colour):
                    moves.append((x, y))

        return moves
