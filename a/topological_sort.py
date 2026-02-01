# recursive dfs topsort
# same as my reversed(dfs(G))
# because it produces increasing post-order numbers, while topsort is decreasing post-order numbers
def topological_sort(G: list[list[int]]) -> list[int]:
    i = 0
    arr = [-1 for _ in range(len(G))]
    visited = set()

    def explore(v: int):
        nonlocal i

        visited.add(v)

        for w in G[v]:
            if w not in visited:
                explore(w)
        arr[-i - 1] = v
        i += 1

    for v in range(len(G)):
        if v not in visited:
            explore(v)
    return arr
