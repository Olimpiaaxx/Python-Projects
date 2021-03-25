class Solution:
    def sameWord(self, str1, str2):


        str1 = list(str1)
        str2 = list(str2)
    
        if len(str1) != len(str2):
            return False


        for i in range(len(str1)):
            if str1[i] == str2[i]:
                continue
            else:
                return False
        return True





                    











#SOLUTION

word1 = 'sylan'
word2 = 'ylan'

my_solution = Solution()

print(my_solution.sameWord(word1, word2))
