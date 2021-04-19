class Checker:
    def __init__(self, board, winning_counter):
        self.board = board
        self.winning_counter = winning_counter

    def check(self, x, y):
        check_pawn = self.board.get(x, y)
        counter = 1

        #right = check_pawn == self.board.get(x, y +1)
        #left = check_pawn == self.board.get(x, y -1)

        while check_pawn == self.board.get(x, y +1):
            counter += 1
            if counter == self.winning_counter:
                return 'you won'
        return 'you lost'


    #    if check_pawn == self.board.get(x +1, y):
    #        counter += 1
    #        if counter == self.winning_counter:
    #            return 'you won'
    #    return 'you lost'



        #if right:
        #    counter += 1
        #if left:
        #    counter += 1


        #return counter == self.winning_counter
