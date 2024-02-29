# Title: Cracking the Sudoku Code: Validating Your 9x9 Board

Sudoku, a game of numbers and logic, has captivated minds worldwide for decades. But what happens when you're faced with a Sudoku board that needs validation rather than solution? In this blog post, we'll dive into the intricacies of validating a 9x9 Sudoku board and explore a Pythonic solution to tackle this challenge.

## Understanding the Problem 🧩

Given a partially filled 9x9 Sudoku board, the task is to determine whether it adheres to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

### The Solution Approach 🛠️

To validate the Sudoku board, we need to keep track of the digits seen in each row, column, and 3x3 sub-box. We'll utilize sets to efficiently check for repetitions.

### Implementation in Python 🐍

Let's take a look at the Python function `isValidSudoku(board)`:

```python
import collections

def isValidSudoku(board: List[List[str]]) -> bool:
    # Initialize sets to keep track of digits in each row, column, and 3x3 sub-boxes
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)  # key = (r / 3, c / 3)

    # Iterate through each cell of the board
    for r in range(9):
        for c in range(9):
            # Check if the cell is empty
            if board[r][c] == ".":
                continue
            
            # Check if the digit is already present in the same row, column, or 3x3 sub-box
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False  # If the digit violates Sudoku rules, return False
            
            # Add the digit to the corresponding sets for rows, columns, and sub-boxes
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True  # If all digits adhere to Sudoku rules, return True
```

### Explaining the Code 📝

- We start by initializing sets to keep track of digits in each row, column, and 3x3 sub-boxes.
- Then, we iterate through each cell of the board.
- For each cell, we check if it's empty. If not, we proceed to validate the digit.
- If we encounter a digit that violates any of the Sudoku rules, we return `False`.
- Otherwise, if all digits adhere to the rules, we return `True`.

### Time and Space Complexity Analysis ⏰

- **Time Complexity**: The time complexity of this solution is O(1) since the Sudoku board is always 9x9, and we iterate through each cell only once.
- **Space Complexity**: The space complexity is also O(1) as we are using a fixed-size data structure (defaultdict) that doesn't depend on the size of the input.

### Conclusion 🎉

Validating a Sudoku board is a classic problem that demonstrates the application of sets and efficient data structure usage. With the provided Python solution, you can now confidently verify the validity of any 9x9 Sudoku puzzle. Whether you're a Sudoku enthusiast or a programming aficionado, mastering this problem opens doors to deeper understanding of logic and algorithmic thinking. Happy Sudoku solving!

**Reference**: [Valid Sudoku - LeetCode](https://leetcode.com/problems/valid-sudoku/)
