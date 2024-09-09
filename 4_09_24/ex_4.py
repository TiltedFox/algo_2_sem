class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        mtrx = [[0 for i in range(n)] for i in range(n)]

        for i in range(len(trust)):
            start = trust[i][0]
            end = trust[i][1]
            mtrx[start - 1][end - 1] = 1

        for i in range(n):
            s = 0
            for j in range(n):
                s += mtrx[j][i]
            if s == n - 1 and not(1 in mtrx[i]):
                return i + 1
        return -1