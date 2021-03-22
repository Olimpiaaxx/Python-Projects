class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        my_dict = {}
        n = list(str(n))
        for i in n:
            char = 1
            if char not in my_dict:
                my_dict.update({char : 1})
            else:
                my_dict[char] += 1
        return my_dict.values()







        
        n = list(str(n))

        counter = 0
        for i in n:
            if i == '1':
                counter += 1
        return counter







#SOLUTION

test_list = 0o0000000000000000000000000001011
test_list2 = 21451

my_solution = Solution()

print(my_solution.hammingWeight(test_list))
