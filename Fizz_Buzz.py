class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[""]*n
        for i in range(1, n+1):
            if i%15==0:
                l[i-1]= "FizzBuzz"
            else:
                if i%3==0:
                    l[i-1] = "Fizz"
                elif i%5==0:
                    l[i-1]= "Buzz"
                else:
                    l[i-1]= str(i)
        return l