"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
#o（n) time | O(1) space
def removeKthNodeFromEnd(head, k):
	counter = 1
	first = head
	second = head
	while counter <= k:
		second = second.next
		counter += 1
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next

#递归
"""
我的理解：先通过head.next = self.removeNthFromEnd(head.next,n)，找到base case也就是if head is None时，设i=0.
然后通过递归慢慢向前并每次加一，找到倒数第n个节点，并且返回这个要删除节点的next。
如果i!=n，也就是这个节点要保留，返回这个节点（通过.next也包括了他后面的那些节点）。
返回节点时会通过head.next = self.removeNthFromEnd(head.next,n)把每次返回的节点接到head.next上。

我认为这个算法比我上面的好在于：
无论要删掉的是最后一个还是第一个节点，都可以通过return head.next if i==n else head返回正确的节点。
比如n=1时删掉最后一个节点，head(倒数第二个节点).next = head(倒数第一个节点).next，也就是None。
如果删掉第一个，就是返回head.next，不需要像我上面的解法1，多一个判断条件。
"""
class Solution:
    def removeNthFromEnd(self, head, n):
        global i
        if head is None:
            i=0
            return None
        head.next = self.removeNthFromEnd(head.next,n)
        i+=1
        return head.next if i==n else head

"""
1.定义一个头结点，指向链表的第一个结点（不再像1.0版一样计算链表长度）
2.快慢指针指向头结点
3.快指针先走n步
4.快慢指针一起走，直到快指针走到链表尾
5.慢指针后一位连接为其后一位的后一位（实现截断连接）
6.返回头结点的后一位结点。
 
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Node = ListNode(None)
        Node.next = head
        first, slow = Node, Node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        return Node.next

 