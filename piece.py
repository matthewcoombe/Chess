class Piece:

    def __init__(self, position: tuple, colour: str, pieceID: str):
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]
        self.colour = colour
        self.pieceID = pieceID

    def possibleMoves(self, grid: list):
        pass

    def getPosition(self):
        return self.position

    def updatePosition(self, position: tuple):
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]

    def getColour(self):
        return self.colour

    @staticmethod
    def inRange(x: int, y: int):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        return False

    def getID(self):
        return self.pieceID

