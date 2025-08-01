from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prev:
                return [prev[diff], i + 1]
            prev[n] = i + 1
        return[]