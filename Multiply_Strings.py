class Solution(object):
    def multiply(self, num1, num2):
        def convert(s):
            sum=0
            nums=[str(digit) for digit in range(10)]
            for i in range(len(s)):
                for j in range(10):
                    if s[i]==nums[j]:
                        sum=sum*10+j
            return sum
        return str(convert(num1)*convert(num2))