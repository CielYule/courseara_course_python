    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x : x[1])
        n = len(intervals)
        cnt = [0] * n

        ans = 0
        for i in range(n):
            interval = intervals[i]
            if cnt[i] == 0:
                pos = i + 1
                while pos < n and intervals[pos][0] <= interval[1]:
                    cnt[pos] += 1
                    if (intervals[pos][0] < interval[1]):
                        cnt[pos] += 1
                    pos += 1
                ans += 2
            elif cnt[i] == 1:
                pos = i + 1
                while pos < n and intervals[pos][0] <= interval[1]:
                    cnt[pos] += 1
                    pos += 1
                ans += 1
        return ans
