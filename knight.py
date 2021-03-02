from piece import Piece
from typing import List, Tuple


class Knight(Piece):

    def __init__(self, position: tuple, colour: str, pieceID: str):
        super().__init__(position, colour, pieceID)
        self.counter = 0

    def possibleMoves(self, grid):
        moves = []
        movesCheck = [(self.x - 1, self.y - 2), (self.x + 1, self.y - 2), (self.x + 2, self.y - 1),
                      (self.x + 2, self.y + 1), (self.x + 1, self.y + 2), (self.x - 1, self.y + 2),
                      (self.x - 2, self.y + 1), (self.x - 2, self.y - 1)]

        for x, y in movesCheck:
            if self.inRange(x, y) and (grid[x][y] is None or not grid[x][y].getColour() == self.colour):
                moves.append((x, y))

        # for i in movesCheck:
        #     if self.inRange(i) and (
        #             grid[i[0]][i[1]] is None or not grid[i[0]][i[1]] == self.colour):
        #         moves.append(i)

        return moves
