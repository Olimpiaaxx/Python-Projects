class Checker:
    def __init__(self, board, winning_counter):
        self.board = board
        self.winning_counter = winning_counter

    def check(self, x, y):
        check_pawn = self.board.get(x, y)
        counter = 1
        #print('item at x, y - 1 is: ' + self.board.get(x, y))
        right = check_pawn == self.board.get(x, y +1)
        left = check_pawn == self.board.get(x, y -1)

        if right:
            counter += 1
        if left:
            counter += 1

        return counter == self.winning_counter
