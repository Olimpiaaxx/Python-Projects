class Solution(object):
    def containsDuplicates(self, nums):
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                return True
        return False



        

        
        
# Solution
test_list = [1, 2, 3, 4, 35, 35]

my_solution = Solution()

print(my_solution.containsDuplicates(test_list))




#back_index = len(nums) - 1
 #       for i in range(len(nums)):
  #          if nums[(back_index - i)] in nums[(back_index - i + 1):]:
   #             nums.remove(nums[(back_index - i)])
#
 #       return len(nums)
