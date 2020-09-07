class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        c = sum(nums) # 奇数直接排除
        if c % 2 != 0:
            return False
        c = c // 2
        w = [False] * (c + 1)
# 第0个位置设置为true，表示当元素出现的时候让w[i-num]为True,也就是w[i]为T
        w[0] = True
        for num in nums:
            for i in range(c, num - 1, -1):
                 w[i] = w[i] or w[i - num]
        return w[c]


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2 == 1: return False
        s = s/2
        n = len(nums)
        dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
        #dp[i][j] 能否用前i个数字，加起来为j
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
        for j in range(1, s + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            for j in  range(1, s + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
        return dp[n][s]





def canPartition(self, nums) -> bool:
  s = sum(nums)
  if s%2 == 1:
    return False
  s = s//2
  n = len(nums)
  dp = [False for _ in range(s + 1)]
  dp[0] = True
  for num in nums:
    for j in reversed(range(1, s + 1)):
      if j >= num:
        dp[j] = dp[j] or dp[j - num]
  return dp[s]