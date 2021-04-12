class Board:
    def __init__(self):
        self.board = []

    def initialize(self):
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append('e')
            self.board.append(temp)

    def is_empty(self, x, y):
        return self.board[x][y] == 'e'

    def put(self, x, y, pawn):
        self.board[x][y] = pawn

    def get(self, x, y):
        return self.board[x][y]

    def show(self):
        for list in self.board:
            for i in range(len(list)):
                if i == len(list) -1:
                    print(list[i], end='')
                else:
                    print(list[i] + ' | ', end='')
            print('')


b = Board()
b.initialize()
b.show()
print(b.is_empty(1, 1))
b.put(1, 1, 'x')
print(b.is_empty(1, 1))
b.show()
print(b.get(1, 2))
