import heapq

def dijistra(graph,start):
    dist = {node : float('inf') for node in graph}
    dist[start] = 0
    parent = {node : None for node in graph}

    pq = [(0,start)]

    while pq:
        current_dis,node = heapq.heappop(pq)
        if current_dis > dist[node]:
            continue
        for neighbour,weight in graph[node]:
            new_dist = current_dis + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                parent[neighbour] =  node
        
            heapq.heappush(pq,(new_dist,neighbour))
    return dist,parent

def shortestpath(parent,start_node,target_node):
    path =[]
    while target_node is not None:
        path.append(target_node)
        target_node = parent[target_node]
    path.reverse()
    return path if path[0] == start_node else []




graph = {
    'A' : [('B', 4),('C',2)],
    'B' : [('C' , 5),('D',10)],
    'C' : [('E',3)],
    'D':[],
    'E':[('D',4)]    
}


start_node = 'A'
target_node = 'D'

dist,parent = dijistra(graph,start_node)
path = shortestpath(parent,start_node,target_node)

if path:
    print(f"Shortest path from {start_node} to {target_node}: {path}")

    print(f"Path from {start_node} to {target_node} : {path}")
    print(f"Distance{dist[target_node]}")
else:
    print("not find the shortestpath")

    
# Found in O((V + E) log V) time and O(V + E) space.

# # | Aspect       | Complexity                          | Explanation                     |
# | ------------ | ----------------------------------- | ------------------------------- |
# | **Time**     | O((V + E) log V)                    | Using heap-based priority queue |
# | **Space**    | O(V + E)                            | Graph + helper structures       |
# | **Best for** | Non-negative weights, sparse graphs |                                 |
# # 