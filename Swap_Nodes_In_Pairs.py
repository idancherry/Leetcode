# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        first=head
        prev=None
        if not head or not head.next:
            return head
        second=head.next
        head=second
        while True:
            first.next=second.next
            second.next=first
            if prev:
                prev.next=second
            prev=first
            first=prev.next
            if not first or not first.next:
                return head 
            second=first.next
        return head