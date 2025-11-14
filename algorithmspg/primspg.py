def prim_simple(n, edges):
    INF = float('inf')

    # Build adjacency matrix
    graph = [[INF]*n for _ in range(n)]
    for w, u, v in edges:
        graph[u][v] = w
        graph[v][u] = w

    selected = [False]*n
    selected[0] = True  # start from node 0
    mst = []
    total_weight = 0

    for _ in range(n-1):
        min_edge = (None, None, INF)  # (u, v, weight)
        for u in range(n):
            if selected[u]:
                for v in range(n):
                    if not selected[v] and graph[u][v] < min_edge[2]:
                        min_edge = (u, v, graph[u][v])
        u, v, w = min_edge
        if v is not None:
            selected[v] = True
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


# Example usage
edges = [
    (1, 0, 1),
    (2, 0, 2),
    (3, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]
n = 4

mst, total_weight = prim_simple(n, edges)
print("MST:", mst)
print("Total weight:", total_weight)

# 📌 Summary
# Complexity	Result
# Time	O(n³)
# Space	O(n²)