# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a map to store the previous numbers and their indices.
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            # Get the difference between the target and the current number.
            diff = target - n

            # If the difference is in the map, return the indices.
            if diff in prevMap:
                return [prevMap[diff], i]

            # Otherwise, add the current number (and it's index) to the map.
            prevMap[n] = i
