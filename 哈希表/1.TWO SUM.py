def twoSum(self, nums, target):
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, j in enumerate(nums):
            if target - j in dic:
                return [dic[target - j], i]
            else:
                dic[j] = i
                #(k,v)键值对 i是索引
