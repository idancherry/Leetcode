# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head and head.val==val:
            head = head.next
        
        curr = head
        if not head or not curr.next:
            return head
        nextnode = curr.next
        while nextnode:
            if nextnode.val == val:
                nextnode = nextnode.next
                curr.next = nextnode
                
            else:
                curr = nextnode
                nextnode = nextnode.next

        return head