class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums3 = []
        nums1.sort()
        nums2.sort()

        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                pass
            else:
                nums3.append(nums2[i])
                #nums2.remove(nums2[i])
                
           # if nums1[i] in nums2:
              #  nums3.append(nums1[i])
             #   nums1.remove(nums1[i])
            return nums3
            



#Solution

ls1 = [4, 9, 5]
ls2 = [9, 4, 9, 8, 4]


my_solution = Solution()
print(my_solution.intersect(ls1, ls2))
