class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def accum(node):
            i=1
            num=0
            curr=node
            while curr:
                num+=curr.val*i
                i*=10
                curr=curr.next
            return num
        head=ListNode(-1)
        curr=head
        for i in str(accum(l1)+accum(l2))[::-1]:
            curr.next=ListNode(int(i))
            curr=curr.next
        return head.next