class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #haystack = list(haystack)
       # needle = list(needle)

       if not needle:
                return 0

       for i in range(len(haystack)):
           if needle[0] == i:
               return haystack.index(needle[0])
               
           #for n_char in needle:
              # if n_char == h_char:
                  # return haystack.index(n_char)
       return -1

        


        #if needle in haystack:
          #  return haystack.index(needle)
       # return -1
            
            









#SOLUTION

word1 = 'hello'
word2 = 'll'

my_solution = Solution()
print(my_solution.strStr(word1, word2))
