__author__ = 'Young'
#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

#If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

#You may not alter the values in the nodes, only nodes itself may be changed.

#Only constant memory is allowed.

#For example,
#Given this linked list: 1->2->3->4->5

#For k = 2, you should return: 2->1->4->3->5

#For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution025:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        length = 0
        current = head
        while current and length < k:
            length += 1
            current = current.next

        if k>length: return head

        current = head
        prev = None
        count = 1
        while count <= k:
            nextCurrent = current.next
            if prev: current.next = prev
            prev = current
            current = nextCurrent
            count += 1
        head.next = self.reverseKGroup(current, k)
        return prev