def topological_sort(graph: list[int]):
    visited = [False] * len(graph)
    order = []
    
    def dfs(v):
        visited[v - 1] = True
        for u in graph[v]:
            if not visited[u - 1]:
                dfs(u)
        order.append(v)

    for v in range(len(visited)):
        if not visited[v - 1]:
            dfs(v)

    return order[::-1]

def arrEdg_to_arrAdj(array: list):
    n = max(max(array))
    arr = [[] for _ in range(n)]

    for i in range(len(array)):
        start = array[i][0]
        end = array[i][1]
        arr[start - 1].append(end)
    return arr


graph = [[7, 0], [5, 6], [3, 8], [3, 7], [8, 0], [4, 2], [4, 6], [2, 6], [2, 8]]
cl = {0: "Пиджак",
      1: "Часы",
      2: "Брюки",
      3: "Рубашка",
      4: "Трусы",
      5: "Носки",
      6: "Туфли",
      7: "Галстук",
      8: "Ремень"}

graph = arrEdg_to_arrAdj(graph)
ord = topological_sort(graph)
for elem in ord:
    print(cl[elem], end = ", ")