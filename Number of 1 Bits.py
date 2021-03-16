class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))

        counter = 0
        for i in n:
            if i == '1':
                counter += 1
        return counter







#SOLUTION

test_list = 0o0000000000000000000000010000000
test_list2 = 21451

my_solution = Solution()

print(my_solution.hammingWeight(test_list))
