from collections import deque

class Solution(object):
    def rotate(self, nums, k):
	    for i in range(k):
		    temp = [nums[-1]]
		    nums = temp + nums[:-1]
		    
		    
		    print(nums)


class Solution2(object):
    def rotate(self, nums, k):
        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]




        
      #  nums.reverse()
       # nums = nums[::k]
        #print(nums)
       # nums = nums[::nums]
        

# Solution
test_list = [1, 2, 3, 4, 5, 6, 7]
k = 3

my_solution = Solution2()
my_solution.rotate(test_list, k)
print(test_list)
