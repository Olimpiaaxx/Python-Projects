class Solution(object):
    def containsDuplicate(self, nums):
       nums.sort()
    for i in range(len(nums)):
            if i == 0:
                pass
            else:
                if nums[i] == nums[i-1]:
                        return True
    return False
        




# Solution
test_list = [1, 2, 44, 2]

my_solution = Solution()

print(my_solution.containsDuplicate(test_list))
