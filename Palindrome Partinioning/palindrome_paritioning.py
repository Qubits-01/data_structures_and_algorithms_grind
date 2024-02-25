# Ref: https://leetcode.com/problems/palindrome-partitioning/description/


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results, part = [], []

        def depth_first_search(i):
            if i >= len(s):
                results.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i : j + 1])
                    depth_first_search(j + 1)
                    part.pop()

        depth_first_search(0)

        return results

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True
