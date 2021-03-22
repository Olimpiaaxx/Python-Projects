class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #haystack = list(haystack)
       # needle = list(needle)

        if not needle:
                return 0

        #for h_char in haystack:
           # print(h_char)

        for n_char in needle:
            if n_char in haystack:
                return haystack.index(n_char)
            else:
                return -1
            
            









#SOLUTION

word1 = 'helo'
word2 = 'll'

my_solution = Solution()
print(my_solution.strStr(word1, word2))
