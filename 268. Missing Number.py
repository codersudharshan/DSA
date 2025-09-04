from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = n * (n + 1) // 2
        actual_sum = sum(nums)
        expected_sum = summ - actual_sum
        return expected_sum