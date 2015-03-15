__author__ = 'Young'
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        answerl = l3
        jinwei = 0
        while l1 != None and  l2 != None:
            number = l1.val + l2.val + jinwei
            l3.next = ListNode(number%10)
            l3 = l3.next

            jinwei = number / 10
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            number = l1.val + jinwei
            l3.next = ListNode(number%10)
            l3 = l3.next

            jinwei = number / 10
            l1 = l1.next

        while l2 != None:
            number = l2.val + jinwei
            l3.next = ListNode(number%10)
            l3 = l3.next

            jinwei = number / 10
            l2 = l2.next

        if jinwei != 0:
            l3.next = ListNode(jinwei)

        return answerl.next


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

test = Solution()
l1 = ListNode(9)
l1.next = ListNode(8)
#l1.next.next = ListNode(9)

l2 = ListNode(1)
#l2.next = ListNode(1)
#l2.next.next = ListNode(1)

x =  test.addTwoNumbers(l1,l2)
while x != None:
    print x.val
    x = x.next
