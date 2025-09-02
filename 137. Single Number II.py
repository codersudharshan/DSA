from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for c in seen:
            if seen[c] == 1:
                return c
