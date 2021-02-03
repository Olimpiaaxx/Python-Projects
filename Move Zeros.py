class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        temp_list = []
        for i in range(len(nums)):
            if nums[i] == 0:
                temp_list.append(nums[i])
            else:
                continue
        new_list = nums + temp_list
        print(new_list)




# Solution
test_list = [0, 1, 0, 3, 12]

my_solution = Solution()

my_solution.moveZeroes(test_list)
