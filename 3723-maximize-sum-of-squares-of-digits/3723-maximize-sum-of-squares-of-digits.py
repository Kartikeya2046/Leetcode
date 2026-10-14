class Solution(object):
    def maxSumOfSquares(self, num, sum):
        result = self.largest_number(num, sum)
        if result == -1:
            return ""            # no valid number exists
        return result

    def largest_number(self, n, s):
        # Feasibility checks
        if s > 9 * n:
            return -1            # not possible
        if s == 0:
            return "0" if n == 1 else -1   # leading zero not allowed

        digits = []
        for _ in range(n):
            d = min(9, s)        # take the biggest digit we can
            digits.append(str(d))
            s -= d               # reduce the remaining sum

        return "".join(digits)