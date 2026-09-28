class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        sign = -1 if x < 0 else 1
        limit = INT_MAX if sign == 1 else -INT_MIN 
        x = abs(x)
        rev = 0

        while x:
            d = x % 10
            x //= 10

            
            if rev > limit // 10 or (rev == limit // 10 and d > limit % 10):
                return 0

            rev = rev * 10 + d

        return sign * rev
