class Solution(object):
    def singleNumber(self, nums):
        single_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] = 0 and nums[i] == len(nums) -1:
                pass
            elif nums[i] == nums[i] -1 and nums[i] == nums[i] +1:
                pass
            else:
                single_list.append(nums[i])
        return single_list
    
# Solution
test_list = [2, 2, 3, 3, 4, 5, 5]

my_solution = Solution()

print(my_solution.singleNumber(test_list))



