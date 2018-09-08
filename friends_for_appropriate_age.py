class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ret = 0
        counter = [0]*121
        for a in ages:
            counter[a] += 1
        for A in range(1, 121):
            for B in range(A + 1):
                if B <= 0.5 * A + 7:
                    continue
                if B > 100 and A < 100:
                    continue
                if counter[A] > 0 and counter[B] > 0:
                    ret += counter[A]*counter[B]
                    if A == B:
                        ret -= counter[A]
        return ret
