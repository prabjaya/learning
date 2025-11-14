def kruskal(n,edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        root_x,root_y = find(x),find(y)
        if root_x == root_y:
            return False
        

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_y] > rank[root_x]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] +=1
        return True
    edges.sort()

    mst , total_weight = [],0

    for wt,u,v in edges:
        if union(u,v):
            mst.append((u,v,wt))
            total_weight += wt
    return mst,total_weight

edges = [
    (1,0,1),
    (2,0,2),
    (3,1,2),
    (4,1,3),
    (5,2,3)
]

mst,total_weight = kruskal(4,edges)
print("mst", mst)
print("total_weight = ", total_weight)