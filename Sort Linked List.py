# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
 
        
        if head < head.next:
            head.self.next
        else: 
            head.next = head


ls = [4, 2, 1, 3]

my_solution = Solution()
print(my_solution.sortList(ls))
