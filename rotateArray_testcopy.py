class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
nums = [1, 2, 3, 4, 5, 6, 7]

temp = [nums[-1]]

ls = temp + nums[:-1]
		
print(ls)


# Solution
test_list = [1,2,3,4,5,6,7]
k = 3

my_solution = Solution()
my_solution.rotate(test_list, k)
#print(test_list)
