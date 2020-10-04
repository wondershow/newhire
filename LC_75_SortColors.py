class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Invariant: 
        nums[0...left] = 0
        nums[left + 1, i - 1] = 1
        nums[i, ... right] unknown
        nums[right + 1.. -1] = 2
        """
        left, right, i = 0, len(nums) - 1, 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left, i = left + 1, i + 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right = right - 1
            else:
                i += 1
