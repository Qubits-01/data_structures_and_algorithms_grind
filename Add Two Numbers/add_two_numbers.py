# Ref: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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
