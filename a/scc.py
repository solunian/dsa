# SCCs: output is array of components

# KEY CONCEPT: greatest post-order number node is a source SCC; is sink in reversed graph
# PITFALL: smallest post-order number not necessarily in a sink SCC!
# dfs 1st pass to get post-numbers order
# dfs 2nd pass on G_R reverse graph for SCCs
def kosaraju(G: list[list[int]]) -> list[list[int]]:
    visited = set()

    def explore(G: list[list[int]], arr: list[int], v: int):
        visited.add(v)
        for w in G[v]:
            if w not in visited:
                explore(G, arr, w)
        arr.append(v)

    # dfs pass 1
    order = []  # gives increasing post-order numbers
    for v in range(len(G)):
        if v not in visited:
            explore(G, order, v)

    # reverse graph construction
    G_R = [[] for _ in range(len(G))]
    for v, ws in enumerate(G):
        for w in ws:
            G_R[w].append(v)

    # dfs pass 2
    sccs = []
    component = []
    visited.clear()
    for v in reversed(order):  # reversed for greatest post-order numbers first
        if v not in visited:
            explore(G_R, component, v)
            sccs.append(component.copy())
            component.clear()

    return sccs


# output: array of components, new condensed graph
# def kosaraju_condense(G: list[list[int]]) -> list[list[int]], list[list[int]]: ...
