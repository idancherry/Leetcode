class Solution(object):
    def getIntersectionNode(self, headA, headB):
        currA=headA
        currB=headB
        lA=0
        lB=0
        while currA:
            lA+=1
            currA=currA.next
        while currB:
            lB+=1
            currB=currB.next
        currA=headA
        currB=headB
        i=0
        j=0
        while currA and currB:
            if currA==currB:
                return currA
            if lA>lB and lA-i>lB:
                currA=currA.next
                i+=1
            elif lA<lB and lA<lB-j:
                currB=currB.next
                j+=1
            else:
                currA=currA.next
                currB=currB.next
                j+=1
                i+=1
        return None