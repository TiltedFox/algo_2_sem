from enum import Enum


class Color(Enum):
    WHITE = 1,
    GRAY = 2,
    BLACK = 3,

class Solution:
    def find_cycle_dir(g):
        c = [Color.WHITE] ** len(g)
        def dfs(v):
            if v % 2 == 1:
                c[v] = Color.GRAY
                for u in g[v]:
                    if c[u] == Color.GRAY or (c[u] == Color.WHITE and dfs(u)):
                        return True
                c[v] = Color.BLACK
            return False

        for v in range(1, len(g), 2):
            if c[v] == Color.WHITE and dfs(v):
                return True
        return False