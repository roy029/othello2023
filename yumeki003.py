class AI(object):
    def __init__(self, face, name):
        self.face = face
        self.name = name

    def play(self, board, color):
        while True:
            x = random.randint(0, board.N+1)
            y = random.randint(0, board.N+1)
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
                return (x, y)
