"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        len_s = len(s)
        i = 0

        for char in t:
            if char == s[i]:
                i += 1
            if i == len_s: #是否都对应
                return True
        return False


#方法一：指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = q = 0
        cnt = 0
        while p<len(s) and q<len(t):
            if s[p] == t[q]:
                cnt += 1
                p += 1
            q += 1
        return cnt == len(s)

"""
后续挑战：二分法
用哈希集合hase_set记录下t中每个字符出现过的位置，即最多有26个key
对s中每个字母进行匹配，s[i]一定出现在s[i-1]之后，所以匹配s[i]的时候，应该找hash_set[s[i]]中大于s[i-1]的索引的索引值
我们用匹配左边界的二分法（即匹配第一个大于等于目标值的数），找当前字母索引列表中第一个大于上一个字母索引的值
如果某个匹配到的边界值等于当前字幕索引列表的长度，则表明无法匹配当前字母，返回False
全部成功匹配返回True
"""
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        # 构建t的哈希集合
        hash_set = {}
        for i, word in enumerate(t):
            if word not in hash_set:
                hash_set[word] = [i]
            else:
                hash_set[word].append(i)

        # 匹配
        index = -1
        for word in s:
            if word not in hash_set:
                return False
            # 字母s出现的索引 用二分法找到其中大于index的第一个
            indexes = hash_set[word]
            left = 0
            right = len(indexes)
            while left < right:
                mid = left + (right - left) // 2
                if indexes[mid] > index:
                    right = mid
                else:
                    left = mid + 1
            if left == len(indexes):
                return False
            index = indexes[left]

        return True
