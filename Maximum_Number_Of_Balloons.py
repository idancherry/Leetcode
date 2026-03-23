class Solution(object):
    def maxNumberOfBalloons(self, text):
        l=["b","a","l","o","n"]
        dic={}
        for i in text:
            dic[i]=dic.get(i,0)+1
        
        for i in l:
            if not i in dic.keys():
                return 0

        return min(dic['b'], dic['a'], int(dic['l']/2), int(dic['o']/2), dic['n'])