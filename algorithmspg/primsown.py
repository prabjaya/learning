def prims(n,edges):
    INF =float('inf')
    graph = [[INF]*n for _ in range(n)]
    for w,u, v in edges:
        graph[u][v] = w
        graph[v][u] = w

    mst =[]
    total_dist = 0
    selected = [False] * n
    selected[0] = True

    for _ in range(n-1):
        min_edge = (None,None,INF)
        for u in range(n):
            if selected[u]:
                for v in range(n):
                    if not selected[v] and graph[u][v] < min_edge[2]:
                        min_edge = ((u,v,graph[u][v]))
        u,v,w = min_edge
        if v is not None:
            selected[v] = True
            mst.append((u,v,w))
            total_dist += w
    return mst,total_dist


edges = [
    (1,0,1),
    (2,0,2),
    (3,1,2),
    (4,1,3),
    (5,2,3)
]

mst,total_dist = prims(4,edges)

print("mst=", mst)
print("total_dist=", total_dist)