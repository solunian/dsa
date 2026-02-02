from a.dfs import dfs
from a.topological_sort import topological_sort
from a.scc import kosaraju

G = [[1, 2], [2, 3], [4, 5], [], [], [], [7], [6]]
dag0 = [[1, 2], [2, 3], [4, 5], [], [], []]
cycle_G = [[1], [2], [0]]

G2 = [
    [4],
    [0, 2, 4, 5],
    [1, 3, 6, 7],
    [7, 8],
    [0],
    [6, 10],
    [8],
    [10],
    [7],
    [8],
    [6],
    [8, 9],
]

print(dfs(G))
print(dfs(cycle_G))
print(topological_sort(dag0))

print(kosaraju(G))
print(kosaraju(cycle_G))
print(kosaraju(G2))
