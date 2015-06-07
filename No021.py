__author__ = 'Young'
#Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution021:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):

        p1 = l1
        p2 = l2
        head = ListNode(0)
        pre = head

        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                pre.next = p1
                p1 = p1.next
            else:
                pre.next = p2
                p2 = p2.next
            pre = pre.next

        if p1 == None:
            pre.next = p2
        else:
            pre.next = p1

        return head.next

