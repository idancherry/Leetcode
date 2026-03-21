# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        size=0
        curr=head
        while curr:
            size+=1
            curr=curr.next
        if size<2:
            return None
        if n==size:
            return head.next
        curr=head
        for i in range(1,size+1):
            if i==size-n:
                toremove=curr.next
                if not toremove:
                    return None
                curr.next=toremove.next
                return head
            curr=curr.next