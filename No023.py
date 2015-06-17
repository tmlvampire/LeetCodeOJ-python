__author__ = 'Young'

#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution023:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):

        answer = self.divideConquer(lists, 0, len(lists))

        return answer

    def divideConquer(self, lists, left, right):
        length = right - left
        if length == 1:
            return lists[left]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[left], lists[right-1])
        if len(lists) > 2:
            answer1 = self.divideConquer(lists, left, (left+right)/2)
            answer2 = self.divideConquer(lists, (left+right)/2, right)
            return self.mergeTwoLists(answer1, answer2)

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