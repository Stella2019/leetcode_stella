"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #create dummy, dummy.next = None
        #starting from node.val = 1
        # dummy.next, head.next, head = head, dummy.next, head.next
        #dummy -> 1 -> Null
        #iteration head = 2, dummy.next = 1
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1, p2 = None, head
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1




def reverseList(head: ListNode) -> ListNode:
    """  循环迭代 """
    pre, cur = None, head
    while cur is not None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre




def reverseList_01(head: ListNode) -> ListNode:
    """
    - 循环迭代2
    - 使用同时赋值
    """
    pre, cur = None, head
    while cur is not None:
        cur.next, pre, cur = pre, cur, cur.next
    return pre


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        - 使用循环能解决，使用递归也能够解决
        - 递归层操作：循环修改相邻两个元素指针指向，使得后一个节点指针指向前一个节点
        - 递归退出条件：递归推出条件其实也是使用循环时退出条件，cur is None，也就是后一个节点为空节点时退出递归。
        """
        def helper(pre, cur):
            if cur is None:
                return pre
            cur_next = cur.next
            cur.next = pre
            return helper(cur, cur_next)
        return helper(None, head)
