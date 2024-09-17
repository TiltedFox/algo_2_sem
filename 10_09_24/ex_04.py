class Solution:
    def findCircleNum(self, graph: list[list[int]]) -> int:
        visited = [False] * len(graph)
        amount = 0

        def dfs(v):
            visited[v] = True
            for i in range(len(graph[v])):
                if graph[v][i] and not(visited[i]):
                    dfs(i)
            return 1

        for v in range(len(visited)):
            if not visited[v]:
                amount += dfs(v)
        return amount