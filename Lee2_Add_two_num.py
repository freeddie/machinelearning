#encoding:utf-8
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        carry = 0
        while True:
        	#按位相加
        	c1 = l1.val if l1 else 0
        	c2 = l2.val if l2 else 0

        	N = c1 + c2 + carry
        	#处理下一个node的值与进位
        	if N > 9:
        		val = N % 10
        		carry = n / 10
        	else:
        		val = N
        		carry = 0
        	#相加节点移位
        	l1 = l1.next if l1 else None
        	l2 = l2.next if l2 else None
        	#先赋值，后移位
        	ptr = ptr.ListNode(val)
        	ptr = ptr.next
        	if not l1 and not l2:
        		if carry:
        			ptr.next = ListNode(carry)
        			ptr = ptr.next
        		break
        return dummyRoot.next
