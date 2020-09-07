"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
#SPACE O(N/2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 将前半个链表放在堆栈里
        fast = slow = ListNode(0)
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next  # 2 times speed

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True


#O(1) 空间复杂度
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # 计算长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 取出后半部分
        length1 = length // 2 if length % 2 == 0 else (length-1) // 2
        new = head
        while length1 > 0:
            new = new.next
            length1 -= 1

        # 反转后半部分
        prev = None
        while new:
            temp = new.next
            new.next = prev
            prev = new
            new = temp

        # 与前半部分逐项对比
        prev_c, head_c = prev, head
        while prev_c:
            if prev_c.val != head_c.val:
                return False
            prev_c = prev_c.next
            head_c = head_c.next
        return True
"""
方法三：反转
算法
step1: 依然利用快慢指针slow和fast，慢指针在辅助指针temp和prev的帮助下边走边反转。当快指针走到底时，链表的前半边已经是反转后的了。
step2: 指针node1和node2从链表的中间分别向两边移动，并比较是否相等。
step3: (optional) 最终，借助step1的slow和prev指针，把链表恢复成原来的序列。
依旧要考虑奇偶，想清楚。
这里设立了flag标注结果，而不是直接return，因为一旦先return了，就不会跑后面的恢复链表算法了。
时间复杂度: O(N); 空间复杂度: O(1)
 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        prev = None
        flag = True
        # step1: reverse
        while(fast and fast.next):
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # step2: compare
        if fast: # 奇数
            node1 = prev
            node2 = slow.next
        else: # 偶数
            node1 = prev
            node2 = slow
        while(node1 and node2):
            if node1.val != node2.val:
                flag = False
            node1, node2 = node1.next, node2.next
        # step3: recover(optional)
        back = slow
        while(prev):
            temp = prev.next
            prev.next = back
            back = prev
            prev = temp
        return flag
"""
方法四：递归
copy官方题解。对于递归算法的底层实现，尤其是堆栈帧(stack frame)有详细的图解。
时间复杂度: O(N); 空间复杂度: O(N)。
"""
def isPalindrome(self, head: ListNode) -> bool:

    self.front_pointer = head

    def recursively_check(current_node=head):
        if current_node is not None:
            if not recursively_check(current_node.next):
                return False
            if self.front_pointer.val != current_node.val:
                return False
            self.front_pointer = self.front_pointer.next
        return True

    return recursively_check()
