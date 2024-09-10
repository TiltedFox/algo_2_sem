class Solution:
    def is_start_end_path(arrAdj: list[list[int]], start: int, end: int):
        def dfs(arr, first, visited=None):
            if visited is None:
                visited = set()

            if first in visited:
                return visited

            for elem in arr:
                if elem[0] == first:
                    for j in range(1, len(elem)):
                        visited.add(first)
                        dfs(arr, elem[j], visited)
            return visited

        # print("1:", dfs(arrAdj, start))
        # print("2:", dfs(arrAdj, end))
        if (end in dfs(arrAdj, start)) and (start in dfs(arrAdj, end)):
            return True
        return False

adj1 = [[1, 2, 3],
        [2, 3],
        [3, 1]]

adj2 = [[1, 2, 3, 5],
        [2, 3],
        [3, 1, 4],
        [4, 5, 6],
        [5, 0],
        [6, 2]]

sol2 = print(Solution.is_start_end_path(adj2, 3, 2))