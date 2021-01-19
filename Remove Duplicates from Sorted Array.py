class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        back_index = len(nums) - 1
        for i in range(len(nums)):
            if nums[(back_index - i)] in nums[(back_index - i + 1):]:
                nums.remove(nums[(back_index - i)])

        return len(nums)
        
# Solution
test_list = [0,0,1,1,1,2,2,3,3,4]

my_solution = Solution()

print(my_solution.removeDuplicates(test_list))
