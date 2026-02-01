# recursive dfs
# produces array by increasing post-order numbers
def dfs(G: list[list[int]]) -> list[int]:
    arr = []
    visited = set()

    def explore(v: int):
        visited.add(v)

        for w in G[v]:
            if w not in visited:
                explore(w)
        arr.append(v)

    for v in range(len(G)):
        if v not in visited:
            explore(v)
    return arr
