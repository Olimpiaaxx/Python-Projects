class Solution(object):
    def firstUniqChar(self, myWord):
        """
        :type s: str
        :rtype: int
        """

        my_dict = {}

        for i in range(len(myWord)):
            if myWord[i] not in my_dict:
                my_dict.update({myWord[i]: 1})
            else:
                my_dict[myWord[i]]+= 1
            
        for character, count in my_dict.items():
            if count == 1:
                return myWord.index(character)
        return -1



# Solution
test_list = 'leetcode'
my_solution = Solution()
print(my_solution.firstUniqChar(test_list))
