class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)

        for i in range(len(nums)):
            if nums[i] != val:
                k += 1

        print(k)
        print(nums[:k])