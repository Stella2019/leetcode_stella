"""
编写一个程序，找到两个单链表相交的起始节点。
要求:时间复杂度为 O(N)，空间复杂度为 O(1)
设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B;同样地，
当访问 B 链表的指针访问 到链表尾部时，令它从链表 A 的头部开始访问链表 A。
这样就能控制访问 A 和 B 两个链表的指针能同时访问到交 点。


我们从A访问再访问B，从B访问再访问A，将得到两个序列:
1. a1, a2, c1, c2, c3, b1, b2, b3, c1, c2, c3
2. b1, b2, b3, c1, c2, c3, a1, a2, c1, c2, c3
可以发现，如果链表A和B有相交的话，一定可以找到相交的节点。



解题思路：
我们通常做这种题的思路是设定两个指针分别指向两个链表头部，一起向前走直到其中一个到达末端，另一个与末端距离则是两链表的 长度差。再通过长链表指针先走的方式消除长度差，最终两链表即可同时走到相交点。

换个方式消除长度差： 拼接两链表。
设长-短链表为 C，短-长链表为 D （分别代表长链表在前和短链表在前的拼接链表），则当 C 走到长短链表交接处时，D 走在长链表中，且与长链表头距离为 长度差;

以下图片帮助理解：当 ha == hb 时跳出，返回即可

"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

#双指针

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        l1 = headA
        l2 = headB
        while l1 != l2:
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = headB
            if l2 is not None:
                l2 = l2.next
            else:
                l2 = headA
        return l1