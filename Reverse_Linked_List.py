# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        curr = head
        nextnode = curr.next
        head.next = None
        while nextnode.next:
            temp = nextnode.next
            nextnode.next = curr
            curr = nextnode
            nextnode = temp
        nextnode.next = curr
        return nextnode