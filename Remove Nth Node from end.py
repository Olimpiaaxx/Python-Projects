#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        





#solution

test_list = [1, 2, 3, 4, 5]
n = 2



h = ListNode(4)
n1 = ListNode(1)
n2 = ListNode(5)
n3 = ListNode(88)
h.next = n1
n1.next = n2
n2.next = n3

curr = h
while curr != None:
	print(curr.val)
	curr = curr.next
	




my_solution = Solution()
#print(my_solution.removeNthFromEnd(test_list, n))
