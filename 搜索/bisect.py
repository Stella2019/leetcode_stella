bisect 模块包含两个主要函数， bisect 和 insort两个函数都利用二分查找算法来在有序序列中查找或插入元素。

bisect 查找

bisect(haystack,needle)在haystack（干草垛）里搜索 needle（针）的位置，该位置满足的条件是，把 needle 插入这个位置之后， haystack 还能保持升序。也就是在说这个函数返回的位置前面的值，都小于或等于 needle 的值。

import bisect
a = [0, 1, 5, 7, 19, 25]
a1 = bisect.bisect(a, 6)

# 这里返回的位置是3是因为：
# 为了保证插入这个数，还能保持列表升序，这个位置显而易见就在值5后面
print(a1)

bisect 函数其实是 bisect_right 函数的别名，后者还有个姊妹函数叫bisect_left。
bisect_left函数是新元素会被放置于它相等的元素的前面，而 bisect_right返回的则是跟它相等的元素之后的位置。

import bisect

a = [0, 4, 5, 7, 19, 25]

# a[2]=5，表示值5的索引位置是2

# 这个返回3，是因为bisect会把新的元素放在相等元素后面即 2 + 1 = 3
a1 = bisect.bisect(a, 5)

# 这个返回2，是因为bisect_left会把新的元素放在相等元素前面即原来值5的索引位置2
a2 = bisect.bisect_left(a, 5)

print(a1, a2) # 3, 2

bisect 可以用来建立一个用数字作为索引的查询表格：

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

#['F', 'A', 'C', 'C', 'B', 'A', 'A']
print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

对于33来说，通过bisect返回的位置是0，所以对应的grades值是[0]=F。
对于99来说，通过bitsect返回的位置是3，所以对应的grades值是[3]=B。

insort 插入

insort(seq, item) 把变量 item 插入到序列 seq 中，并能保持 seq 的升序顺序。

import random
import bisect

my_list = []
for i in range(10):
    new_item = random.randrange(20)
    bisect.insort(my_list, new_item)
print(my_list)











import bisect

a = [1, 4, 6, 8, 12, 15, 20]
position = bisect.bisect(a, 13)
print(position)

# 用可变序列内置的insert方法插入
a.insert(position, 13)
print(a)

import bisect

a = [1, 4, 6, 8, 12, 15, 20]
bisect.insort(a, 13)
print(a)