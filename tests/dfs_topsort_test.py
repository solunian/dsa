from a.dfs import dfs
from a.topological_sort import topological_sort

G = [[1, 2], [2, 3], [4, 5], [], [], [], [7], [6]]
cycle_G = [[1], [2], [0]]

print(dfs(G))
print(dfs(cycle_G))
print(topological_sort(G))
