class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        dict1 = {}
        nums1.sort()
        nums2.sort()

        for i in nums1:
            if i not in dict1:
                dict1[i] = 1   
            else:
                dict1[i] += 1
        nums3 = []

        for i in nums2:
            if i in dict1 and dict1[i]:
                dict1[i] -= 1
                nums3.append(i)

        return nums3
            



#Solution

ls1 = [4, 9, 5]
ls2 = [9, 4, 9, 8, 4]


my_solution = Solution()
print(my_solution.intersect(ls1, ls2))
