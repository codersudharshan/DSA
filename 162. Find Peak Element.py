from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        i, j = 0, len(nums)

        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[mid + 1]:

                j = mid
            else:

                i = mid + 1

        return i