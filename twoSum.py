class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_list = []
        for i in range(len(nums)):
            next_item = i + 1
            if nums[i] + nums[next_item] == target:
                return True
            else:
                continue
                if True:
                    new_list.append(nums[i], nums[next_item])
            return new_list







# Solution
test_list = [3, 2, 4]
target = 6

my_solution = Solution()

print(my_solution.twoSum(test_list, target))
