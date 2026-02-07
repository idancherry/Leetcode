# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1=list1
        curr2=list2
        head=ListNode()
        curr=head
        while (curr1!=None and curr2!=None):
            if curr1.val<curr2.val:
                curr.next=curr1
                curr1=curr1.next
            else:
                curr.next=curr2
                curr2=curr2.next
            curr=curr.next
        curr.next = curr1 if curr2==None else curr2
        return head.next
        