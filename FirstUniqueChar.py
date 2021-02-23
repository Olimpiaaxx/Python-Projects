class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """


        my_dict = {}

        for i in range(len(s)):
            char = s[i]
            if char not in my_dict:
                my_dict.update({char: 1})
            else:
                my_dict[char]+= 1
            for char in range(len(my_dict)):
                if my_dict[char] == 1:
                    print('got it')
    
                
        return my_dict
class Solution2(object):
    def firstUniqChar(self, s):

        s = list(s)
        s.sort()
        for i in range(len(s) -1):
            if s[i] != s[i +1]:
                return i
            else:
                return -1


# Solution
test_list = 'oko'
my_solution = Solution2()
print(my_solution.firstUniqChar(test_list))
