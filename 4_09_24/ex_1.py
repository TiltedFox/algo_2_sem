class Solution:
    def arrAdj_to_mtrxAdj(array: list):
        n = len(array)
        mtrx = [[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            v = array[i]
            for j in range(1, len(v)):
                mtrx[i][v[j] - 1] = 1
        # print(mtrx)
        return mtrx

    def mtrxAdj_to_arrAdj(mtrx: list):
        n = len(mtrx)
        arr = [[] for i in range(n)]

        for i in range(n):
            arr[i].append(i + 1)
            for j in range(n):
                if mtrx[i][j] == 1:
                    arr[i].append(j + 1)
        # print(arr)
        return arr
    
    def arrEdg_to_mtrxAdj(array: list):
        n = max(max(array))
        mtrx = [[0 for i in range(n)] for i in range(n)]

        for i in range(len(array)):
            start = array[i][0]
            end = array[i][1]
            mtrx[start - 1][end - 1] = 1
        # print(mtrx)
        return mtrx

    def mtrxAdj_to_arrEdg(mtrx: list):
        n = len(mtrx)
        array = []

        for i in range(n):
            for j in range(n):
                if mtrx[i][j] == 1:
                    array.append([i + 1, j + 1])
        # print(array)
        return array

    def arrEdg_to_arrAdj(array: list):
        n = max(max(array))
        arr = [[] for i in range(n)]

        for i in range(n):
            arr[i].append(i + 1)
        for i in range(len(array)):
            start = array[i][0]
            end = array[i][1]
            arr[start - 1].append(end)
        # print(arr)
        return arr

    def arrAdj_to_arrEdg(array: list):
        arr = []

        for i in range(len(array)):
            for j in range(1, len(array[i])):
                arr.append([i + 1, array[i][j]])
        # print(arr)
        return arr

# adj = [[1, 2, 3],
#         [2, 3],
#         [3, 1]]
# mtrx = [[0, 1, 1],
#         [0, 0, 1],
#         [1, 0, 0]]
# edg = [[1, 2], [1, 3], [2, 3], [3, 1]]

# sol1 = Solution.arrAdj_to_mtrxAdj(adj)
# sol2 = Solution.mtrxAdj_to_arrAdj(mtrx)
# sol3 = Solution.arrEdg_to_mtrxAdj(edg)
# sol4 = Solution.mtrxAdj_to_arrEdg(mtrx)
# sol5 = Solution.arrEdg_to_arrAdj(edg)
# sol6 = Solution.arrAdj_to_arrEdg(adj)