"""
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

相遇问题
移动距离最小的方式是所有元素移动到中位数，排序找到中位数
"""
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)%2 == 0:
            mid = (nums[len(nums)//2-1] + nums[len(nums)//2])//2
        else:
            mid = nums[len(nums)//2]
        ans = 0
        for num in nums:
            ans += abs(num - mid)
        return ans