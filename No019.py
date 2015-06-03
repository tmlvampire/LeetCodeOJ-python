__author__ = 'Young'

#Given a linked list, remove the nth node from the end of list and return its head.

#For example,

#   Given linked list: 1->2->3->4->5, and n = 2.

#   After removing the second node from the end, the linked list becomes 1->2->3->5.
#Note:
#Given n will always be valid.
#Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution19:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        p0 = head
        p1 = head
        p2 = head
        temp = n - 1
        while temp > 0:
            p2 = p2.next
            temp -= 1
        if p2.next == None:
            return head.next
        while p2.next != None:
            p2 = p2.next
            p0 = p1
            p1 = p1.next

        p0.next = p1.next
        return head