class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i in nums and i == nums[:i]:
                return nums.index(i)

# Solution
test_list = [2, 2, 3]

my_solution = Solution()

print(my_solution.singleNumber(test_list))
