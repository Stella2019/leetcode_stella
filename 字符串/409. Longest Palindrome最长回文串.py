#count 模块
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)
        for key in counter.keys():
            v = counter[key]
            ans += v//2*2
            if ans%2 == 0 and v%2 == 1:
                ans += 1
        return ans


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = {}
        for c in s:
            if c in cnts:
                cnts[c] += 1
            else:
                cnts[c] = 1
        palindrome = 0
        for (key, value) in cnts.items():
            palindrome += math.floor(value / 2) * 2
        if palindrome < len(s):
            palindrome += 1
        return palindrome