# https://leetcode.com/problems/happy-number/

# TODO: Use linked-list (Floyd's Cycle Detection Algorithm) to detect cycles.
# or any other cycle detection algorithm.

from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        # Create a set to store the previous numbers.
        prevSet = set()

        # Loop until the number is 1 or the number is in the set.
        while n != 1 and n not in prevSet:
            # Add the current number to the set.
            prevSet.add(n)

            # Get the sum of the squares of the digits.
            n = sum([int(d) ** 2 for d in str(n)])

        # Return whether the number is 1.
        return n == 1
