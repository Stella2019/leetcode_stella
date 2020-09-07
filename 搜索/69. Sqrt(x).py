"""
二分查找也称为折半查找，每次都能将查找区间减半，这种折半特性的算法时间复杂度为 O(logN)。 m 计算
有两种计算中值 m 的方式:
m = (l + h) / 2 m = l + (h - l) / 2
l + h 可能出现加法溢出，最好使用第二种方式。
一个数 x 的开方 sqrt 一定在 0 ~ x 之间，并且满足 sqrt == x / sqrt。可以利用二分查找在 0 ~ x 之间查找 sqrt。
对于 x = 8，它的开方是 2.82842...，最后应该返回 2 而不是 3。在循环条件为 l <= h 并且循环退出时，h 总是比 l 小 1，也就是说 h = 2，l = 3，因此最后的返回值应该为 h 而不是 l。

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, h = 0, x
        while l <= h:
            m = math.floor(l + (h - l) / 2)
            if x/m >m:
                l=m+1
            elif x / m < m:
                h=m-1
            elif x/m ==m:
                return m
        return h