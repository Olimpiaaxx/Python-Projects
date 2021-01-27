class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)):
            if i >= (len(s) -1 -i):
               break
            temp = s[i]
            s[i] = s[len(s) -1 -i]
            s[len(s) -1 -i] = temp
            



# Solution
test_list = ['h', 'e', 'l', 'l', 'o']

my_solution = Solution()

my_solution.reverseString(test_list)


print(test_list)
