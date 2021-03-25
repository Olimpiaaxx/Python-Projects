class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #haystack = list(haystack)
       # needle = list(needle)

        if not needle:
                return 0

        for char in needle:
            if char not in haystack or len(needle) > len(haystack):
                return -1
            return haystack.index(char)
                   
           #for n_char in needle:
              #  if n_char == h_char:
                  # return haystack.index(n_char)
      #return -1

        


        #if needle in haystack:
          #  return haystack.index(needle)
       # return -1
            
            








#SOLUTION

word1 = 'mississippi'
word2 = 'mississippi'

my_solution = Solution()
print(my_solution.strStr(word1, word2))
