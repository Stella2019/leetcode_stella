#快排 O(N) O(1)
"""class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        return self.quick_sort(nums, k)
    def quick_sort(self, nums, k):
        k = len(nums) - k
        left = 0
        right = len(nums)
"""

# 首先要明确，此题目求的是 第K个最大元素，就是说将数据进行从小到大排序，倒数第K个元素。
class Solution:
    def partition(self, nums, left, right):  # 一次排序
        temp = nums[left]
        while left < right:
            while (left < right) and (nums[right] >= temp):
                right -= 1
            nums[left] = nums[right]
            while (left < right) and (nums[left] <= temp):
                left += 1
            nums[right] = nums[left]
        nums[left] = temp
        return left  # left左边的数字比left小

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums) - 1, k)

    def select(self, nums, left, right, k):
        p = self.partition(nums, left, right)
        m = right - p + 1
        if m == k:
            return nums[p]
        if k > m:  # 此元素在左边
            return self.select(nums, left, p - 1, k - m)
        else:  # 此元素在右边
            return self.select(nums, p + 1, right, k)



#堆排序  O(NLOGK)  O(K)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
         return self.heap_sort(nums, k)

    def heap_sort(self, nums, k):
        #maxheap
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heap_adjust(nums, i, len(nums))

        cnt = 0
        #交换堆顶元素，重新调整结构
        for i in range(len(nums) - 1, 0, -1):
            self.heap_swap(nums, 0, i)
            cnt += 1
            if cnt == k:
                return nums[i]
            self.heap_adjust(nums, 0, i)
        return nums[0]

    def heap_adjust(self, nums, start, length):
        tmp = nums[start]
        k = start * 2 + 1
        while k < length: #对于完全二叉树，没有左节点一点没有右节点
            #当前节点左节点符号
            left = start * 2 + 1
            #当前节点右节点符号
            right = left + 1

            if right < length and nums[right] > nums[left]:
                #如果右节点比较大
                k = right

            if nums[k] > tmp:
                #如果子节点比父节点大，则将子节点复制给父节点
                nums[start] = nums[k]
                start = k
            else:
                break

            k = k * 2+ 1
        nums[start] = tmp

    def heap_swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        return nums

