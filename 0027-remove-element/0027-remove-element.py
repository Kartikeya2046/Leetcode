class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)

        k = 0

        for c in nums:
            if c != val:
                k += 1

        print(k)
        print(nums)
                