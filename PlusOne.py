class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        arr = ''
        for i in range(len(digits)):
            digits[-1] += 1
            if digits[-1] > 9:
                arr = str(digits[-1])
                digits.remove(digits[-1])
                arr2 = list(arr)
                digits += arr2
            return digits

#maybe do another function for the other digits?  [2, 9] = [3, 0]

#Solution

test_list = [2, 9]
9,9

my_solution = Solution()

print(my_solution.plusOne(test_list))
