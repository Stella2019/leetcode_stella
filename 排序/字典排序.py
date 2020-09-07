class Solution(object):
    def topKFrequent(self, nums, k):
        fre_dict = {}
        for num in nums:
            if num not in fre_dict:
                fre_dict[num] = 1
            else:
                fre_dict[num] += 1
        fre_sort = sorted(fre_dict.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(fre_sort[i][0])
        return res

"""
sorted(d.items(), key=lambda x: x[1]) 中 d.items() 为待排序的对象；key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序。 key=lambda  变量：变量[维数] 。维数可以按照自己的需要进行设置。

2、维数以字符串来表示

# 将列表中的age由大到小排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
b=sorted(alist,key=lambda x:x['age'],reverse=True)

"""