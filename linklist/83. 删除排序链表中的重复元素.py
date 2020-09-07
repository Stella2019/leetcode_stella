"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
            #1->1->1->2->3...
                runner = runner.next
            current.next = runner
            current = runner
        return head

"""
标签：链表、假节点
跟 「26.有序数组删除重复元素」有什么相似之处？
26 题，有序数组删除重复元素，可使用「双指针」：不真正删除，找到后面不重复元素，依次覆盖前面元素，最后只返回不重复元素的长度。因为数组有下标，所以「双指针」实现比较简单。
此题需要返回一个没有重复元素的新链表，因为没有链表没有下标，如果使用「双指针」（双引用），后面覆盖前面，可行。但返回新链表，实现起来比较复杂。
此题可借助链表的特性「指针」（Pointer）来实现。如果当前节点的值等于下一个节点的值，指向下下个节点（跳过下一个节点），引用 head 并后移一位。

                 head 
                  ↓    
 dummyHead → 0 -> 1 -> 1 -> 2 -> 3 -> 3 -> None  ∵ head.val == head.next.val  ∴ head.next = head.next.next head = head.next
                   ↘_______↗

                     head 
                       ↓    
 dummyHead → 0 -> 1 -> 2 -> 3 -> 3 -> None
需要考虑特殊情况：有 2 个以上相同的节点。只有当所有相同节点都跳过时，引用 head 才后移

                 head 
                  ↓    
 dummyHead → 0 -> 1 -> 1 -> 1 -> 2 -> None
                   ↘_______↗

                 head 
                  ↓    
 dummyHead → 0 -> 1 -> 1 -> 2 -> None
                   ↘_______↗

                     head 
                       ↓    
 dummyHead → 0 -> 1 -> 2 -> None
时间复杂度：O(n)，链表需要遍历完
空间复杂度：O(1)，不需要额外空间
 
"""
# Python3
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummyHead,dummyHead.next = ListNode(0),head
        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummyHead.next

"""
解法——两步走：
第一步【起始行：while l1 and prev.val == l1.val:】：
暂停指针prev，不断获取l1的next（下一个节点），比较其val直至删除节点到两者的val不相等为止；
第二步【起始行：if l1:】：
滑动指针prev和l1，开始新一轮的"第一步",直到l1为None后退出循环

两个提醒：
1.注意空链表的情况（即[]）；
2.在比较节点的val或滑动节点时注意节点不能为None，该种情况下需要添加is not None的条件判断。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # 如果是空链表
        if head is None:
            return head
        # 创建需要操作的变量l1
        l1 = head
        # 维护一个指针prev
        prev = l1
        l1 = l1.next

        while l1:

            # 比较prev和l1的值是否相等，直到删除至不相等为止
            while l1 and prev.val == l1.val:
                l1 = l1.next
                prev.next = l1

            # 指针顺序滑动
            if l1:
                prev = prev.next
                l1 = l1.next

        # 返回头节点（注意不能返回l1）
        return head

