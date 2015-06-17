__author__ = 'Young'
#Given a linked list, swap every two adjacent nodes and return its head.

#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.

#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution024:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if None == head:
            return None
        first = head
        second = None
        while None != first and None != first.next:
            temp = ListNode(0)
            temp.next = first
            second = first.next
            temp = first.val
            first.val = second.val
            second.val = temp
            first = second.next
        return head



x = Solution024()

a = x.swapPairs()