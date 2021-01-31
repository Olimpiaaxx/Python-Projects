class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check if a list is valid
 
        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue
                
                # first requirement
                if board[i][j] in board[i][:j]:
                    return False
                
                # second requirement
                for k in range(len(board)):
                    if board[i][j] == board[k][j] and k != i:
                        return False
                    
                # third requirement
                # 
                offseti = 0
                offsetj = 0
                if i > 2:
                    offseti = 3
                if i > 5:
                    offseti = 6
                if j > 2:
                    offsetj = 3
                if j > 5:
                    offsetj = 6
                for k in range(3):
                    for l in range(3):
                        if board[i][j] == board[k + offseti][l + offsetj] and (i != k + offseti and j != l + offsetj):
                            return False

       

        return True


                

# Solution
test_list = [["5","3",".",".","2",".",".",".","."],
             [".","2",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".",".",".",".",".","6"],
             [".","6",".",".",".",".",".","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","2"]]


my_solution = Solution()

print(my_solution.isValidSudoku(test_list))

