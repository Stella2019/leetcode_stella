"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

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
        #perhaps no inputs
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        carry = 0 #carry 位
        dummy = ListNode(0);
        p = dummy

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

            #l1: 2->4 ->3
            #l2: 5->6->4->1
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        #最高位溢出
        if carry == 1:
            p.next = ListNode(1)

        return dummy.next


#递归解法：思路就是补头，然后分情况讨论输出。
#为了节省内存，结果存储在链表l1中。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if l1 == None and l2 == None and carry == 0:
            return None

        if l1 == None and l2 == None and carry == 1:
            return ListNode(1)

        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)

        l1.val, carry = (l1.val + l2.val + carry) % 10, (l1.val + l2.val + carry) // 10
        l1.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return l1
