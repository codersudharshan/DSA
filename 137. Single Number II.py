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
##
arr = [1,3,2,4,1,5,3]
n = len(arr)
count = 0

for i in range(1, n - 1):
    if arr[i] < arr[i -1] and arr[i] < arr[i + 1]:
        count += 1
    elif arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
        count += 1
print(count)

