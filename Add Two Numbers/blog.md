# 📝 Mastering Linked Lists Arithmetic: Solving the "Add Two Numbers" Problem 📝

Welcome to another adventure in the realm of data structures and algorithms! Today, we'll delve into the fascinating "Add Two Numbers" problem, a medium-level challenge that tests our ability to perform arithmetic operations on linked lists efficiently.

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. The task is to add the two numbers and return the sum as a linked list.

### Examples

Let's dive into a few examples to understand the problem better:

1. **Example 1:**
    - **Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
    - **Output:** `[7,0,8]`
    - **Explanation:** 342 + 465 = 807.

2. **Example 2:**
    - **Input:** `l1 = [0]`, `l2 = [0]`
    - **Output:** `[0]`

3. **Example 3:**
    - **Input:** `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
    - **Output:** `[8,9,9,9,0,0,0,1]`

### Constraints

- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

## Solution Approach

To solve this problem, we'll traverse both linked lists simultaneously, performing digit-by-digit addition and propagating any carry that occurs. Here's our approach:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    sumHeadNode = ListNode()
    currentNode = sumHeadNode

    carry = 0
    while l1 or l2 or carry:
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0

        # Calculate the new digit.
        val = value1 + value2 + carry
        carry = val // 10
        val = val % 10
        currentNode.next = ListNode(val)

        # Update the pointers.
        currentNode = currentNode.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return sumHeadNode.next
```

## Additional Insights

### Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1 and l2. Since each digit is in the range of 0 to 9, summing two digits may result in an overflow. For example, 5 + 7 = 12. In this case, we set the current digit to 2 and bring over the carry of 1 to the next iteration. The carry must be either 0 or 1 because the largest possible sum of two digits (including the carry) is 9 + 9 + 1 = 19.

The pseudocode is as follows:

- Initialize current node to sum head node of the returning list.
- Initialize carry to 0.
- Loop through lists l1 and l2 until you reach both ends and carry is 0.
  - Set x to node l1's value. If l1 has reached the end, set x to 0.
  - Set y to node l2's value. If l2 has reached the end, set y to 0.
  - Set sum = x + y + carry.
  - Update carry = sum // 10.
  - Create a new node with the digit value of sum % 10 and set it to current node's next, then advance current node to next.
  - Advance both l1 and l2.
- Return dummy head's next node.

### Complexity Analysis

- **Time complexity:** O(max(m,n)), where m and n represent the lengths of l1 and l2 respectively. The algorithm above iterates at most max(m,n) times.
- **Space complexity:** O(1). The length of the new list is at most max(m,n) + 1. However, we don't count the answer as part of the space complexity.

## Conclusion

The "Add Two Numbers" problem challenges us to leverage linked list manipulation and basic arithmetic operations to compute the sum of large numbers efficiently. By implementing a systematic traversal strategy and handling carry propagation effectively, we can achieve accurate results for various test cases. This problem highlights the importance of algorithmic thinking and problem-solving skills in navigating complex challenges.

For further exploration and practice, visit the ["Add Two Numbers" problem on LeetCode](https://leetcode.com/problems/add-two-numbers/). Happy coding! 🚀
