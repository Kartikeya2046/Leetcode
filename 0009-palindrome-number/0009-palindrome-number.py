class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = list(str(x)[::-1])

        if str(x) == ''.join(y):
            return True

        return False