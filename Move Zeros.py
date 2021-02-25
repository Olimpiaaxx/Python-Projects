class Solution(object):
    def moveZeroes(self, nums):
	    last_item = len(nums) -1
	    for i in range(len(nums)):
		    if nums[last_item -i] == 0:
			    temp = nums[last_item - i]
			    nums.remove(nums[last_item -i])
			    nums.append(temp)
			    
	    print(nums)





        
    #    temp_list = []
     #   for i in range(len(nums)):
     #       if nums[i] == 0:
     #           temp_list.append(nums[i])
                
      #  back_index = len(nums) -1
       # for i in range(len(nums)):
       #     if nums[back_index - i] == 0:
        #        nums.remove(nums[back_index - i])

       # new_list = nums + temp_list
        #print(new_list)


# Solution
test_list = [0, 1, 0, 3, 12]

my_solution = Solution()

print(my_solution.moveZeroes(test_list))
