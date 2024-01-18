# https://leetcode.com/problems/valid-anagram/

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a map to store the frequency of each character in s.
        freqMap = {}  # char -> freq

        # Loop through each character in s.
        for char in s:
            # Increment the frequency of the current character.
            freqMap[char] = freqMap.get(char, 0) + 1

        # Loop through each character in t.
        for char in t:
            # Decrement the frequency of the current character.
            freqMap[char] = freqMap.get(char, 0) - 1

        # Loop through each character in the map.
        for char in freqMap:
            # If the frequency is not zero, return False.
            if freqMap[char] != 0:
                return False

        # Return True.
        return True
