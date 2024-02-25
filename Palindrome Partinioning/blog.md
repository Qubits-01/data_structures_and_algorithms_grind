# 📝 Exploring Palindromic Partitioning: Solving the "Palindrome Partitioning" Problem 📝

Welcome to another journey through the realm of algorithms and problem-solving! Today, we're delving into the intriguing "Palindrome Partitioning" problem, a medium-level challenge that tests our ability to partition a string into substrings, each of which forms a palindrome.

## Problem Overview

Given a string `s`, the task is to partition it such that every substring of the partition is a palindrome. Our goal is to return all possible palindrome partitionings of `s`.

### Examples

Let's explore a few examples to better understand the problem:

1. **Example 1:**
    - **Input:** `s = "aab"`
    - **Output:** `[["a","a","b"],["aa","b"]]`

2. **Example 2:**
    - **Input:** `s = "a"`
    - **Output:** `[["a"]]`

### Constraints

- 1 <= s.length <= 16
- `s` contains only lowercase English letters.

## Solution Approach

To tackle this problem, we utilize backtracking through depth-first search (DFS) to explore all possible partitionings of the input string. Let's dive into the solution code and understand it step by step.

```python
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
```

## Solution Explanation

### Overview

- We use a backtracking approach to explore all possible palindrome partitionings of the input string `s`.
- The `partition` function initializes empty lists `results` and `part` to store the final partition results and the current partition being explored, respectively.
- We define a `depth_first_search` function that implements depth-first search (DFS) for backtracking. It recursively explores all possible partitionings starting from a given index `i`.
- Within the `depth_first_search` function, we iterate over possible substring lengths starting from index `i` up to the end of the string.
- For each substring, we check if it is a palindrome using the `isPalindrome` helper function.
- If a palindrome substring is found, it is added to the current partition (`part`), and further exploration continues recursively from the next index (`j + 1`).
- If the end of the string is reached (`i >= len(s)`), the current partition is a valid palindrome partition, and a copy of it is added to the final results (`results`).
- After exploring all possibilities, the function returns the final list of palindrome partitionings.

### Helper Function

- The `isPalindrome` helper function checks if a substring of the input string `s` from index `l` to `r` (inclusive) is a palindrome.

### Function Invocation

- The `depth_first_search` function is initially called with the starting index `0` to initiate the backtracking process.
- The final list of palindrome partitionings stored in `results` is returned by the `partition` function.

## Complexity Analysis

- **Time Complexity**: O(N * 2^N), where N is the length of string `s`. This is the worst-case time complexity when all possible substrings are palindromes.
- **Space Complexity**: O(N), where N is the length of the string `s`. This space will be used to store the recursion stack.

## Conclusion

The "Palindrome Partitioning" problem challenges us to efficiently partition a string into substrings, ensuring that each substring is a palindrome. By leveraging backtracking through depth-first search, we explore all possible partitionings and validate palindromic substrings along the way. While dynamic programming offers a potential optimization for future enhancements, the current approach provides a clear and concise solution to the problem. This problem showcases the power of algorithmic techniques in solving complex string manipulation challenges.

For further exploration and practice, visit the ["Palindrome Partitioning" problem on LeetCode](https://leetcode.com/problems/palindrome-partitioning/). Happy coding! 🚀
