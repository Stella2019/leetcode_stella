class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)] #val, row, col
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
          ret, i, j = heapq.heappop(heap) #i- row , j - col
          if j+1 < len(matrix[0]):
            heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret

    from bisect import bisect
    class solution:
        def kthSmallest(self, matrix, k):
            lo, hi = matrix[0][0], matrix[-1][-1]
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if sum(bisect(row, mid) for row in matrix) < k:
                    lo = mid + 1
                else:
                    hi = mid
            return lo