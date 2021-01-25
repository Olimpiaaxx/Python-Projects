class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check if a list is valid
 
        for ls in board:
            for i in range(len(ls)):
                if ls[i] in ls[:i] and ls[i] != '.':
                    return False

        #for j in range(9):
          #  item_to_compare = board[0][0]
            #for i in range(len(board)):
        #        if board[i][0] == item_to_compare and i != 0:
         ###           return False 
        for i in range(len(board)):
            for j in range(len(board[i])):
              #  print(board[i][j])
                for k in range(len(board)):
                    #print(board[k][j])
                    if board[i][j] == board[k][j] and (k != i and board[i][j] != '.'):
                        #print(i, j, k)
                        return False
                        



        return True

                

# Solution
test_list = [["5","3",".",".","2","1",".",".","."],
             ["3","2",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".",".",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]


my_solution = Solution()

print(my_solution.isValidSudoku(test_list))

