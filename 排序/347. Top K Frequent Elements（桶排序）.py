#桶排序
class Solution:
    def topKFrequent(nums, k):
        maps = {}
        for i in nums:
            maps[i] = maps.get(i, 0) + 1  # 字典映射
        max_time = max(maps.values())
        TongList = [[] for i in range(max_time + 1)]#根据最大次数生成桶
        for key, value in maps.items():
            TongList[value].append(key)  # 将索引value放入key对应的字典索引
        res = []
        for i in range(max_time, 0, -1):  # 按桶索引排序
            if TongList[i]:
                res.extend(TongList[i])
            if len(res) >= k:
                return res[:k]


class Solution:
    def topKFrequent(self, nums:'List[int]', k: 'int') -> 'List[int]':
        frequent_of_number = {}
        for num in nums:
            frequent_of_number[num] = frequent_of_number.get(num, 0) + 1
            #建桶
            buckets = [[] for i in range(len(nums)+ 1)] #如果用[]*(len(nums)+1)则是浅拷贝
            for key, value in frequent_of_number.items():
                buckets[value].append(key)
            print(buckets)
            result = []
            for x in range(len(nums), -1, -1):
                if k > 0 and buckets[x]:
                    result += buckets[x]
                    k -= len(buckets[x])
                if k == 0:
                    return result



#对字典排序
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