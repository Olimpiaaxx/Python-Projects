class Solution:
    def findChar(self, word, char):

        for letter in word:
            if char == letter:
                return word.index(char)











#SOLUTIONS
word = 'Sylan'
char = 'a'

my_solution = Solution()

print(my_solution.findChar(word, char))
