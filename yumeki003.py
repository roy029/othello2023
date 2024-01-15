class AI(object):
    def _init_(self):
        self.name = "yumeki"
        self.face = "🕺"

    def play(self, board, color):
        while True:
            x = random.randint(0, board.N+1)
            y = random.randint(0, board.N+1)
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
                return (x, y)
