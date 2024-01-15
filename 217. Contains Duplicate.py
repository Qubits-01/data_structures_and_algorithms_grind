# Ref: https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Know if there is a duplicate in the list
        # 1. Sort the list
        # 2. Compare the current element with the next element
        # 3. If they are equal, return True
        # 4. If the loop ends, return False

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
