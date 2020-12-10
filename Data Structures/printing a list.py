#  Initial List
nums = [0, 0, 2, 3, 4, 4]
# List of items to remove
nums2 = []
#
# a
# for
# if
#
previous = "a"
for current in nums:
    if current == previous and previous != "a":
        nums2.append(current)
    previous = current
    
#
#
# Removing items in nums2 from nums
for i in nums2:
    nums.remove(i)
print('nums: ', nums)
print('nums2: ', nums2)








### SEPARATE ###
# Printing items in a list
#for i in nums2:
#    print(i)



#spojrzec na liste
#usunac to co sie powtarza


