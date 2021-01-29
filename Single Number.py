class Solution(object):
    def singleNumber(self, nums):
        single_list = []
        nums.sort()
        for i in range(len(nums)):
            #print(i)
            if i == 0 or i == len(nums) -1:
                pass
            elif nums[i] == nums[i -1] or nums[i] == nums[i +1]:
                pass
            else:
                single_list.append(nums[i])
        return single_list[0]
    
# Solution
test_list = [2, 2, 3, 3, 5, 5, 4]
test_list2 = [4, 2, 2, 3, 3, 5, 5]
my_solution = Solution()

print(my_solution.singleNumber(test_list))
print(my_solution.singleNumber(test_list2))



#zeby porownac z poprzednim item to [i -1] a z nastepnym to [i +1]


#ten dzialal na leetcode
new_list = []
for i in range(len(nums)):
    if nums[i] in new_list:
        new_list.remove(nums[i])
    else:
        new_list.append(nums[i])
return new_list[0]
