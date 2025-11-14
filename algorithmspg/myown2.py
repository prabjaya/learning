import heapq

def dijistra(graph, start):
    dist = {node : float ('inf') for node in graph}
    dist[start] = 0
    parent ={node : None for node in graph}

    pq = [(0,start)]

    while pq:
        current_dist,node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        for neighbour,weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                parent[neighbour] = node
                heapq.heappush(pq,(new_dist,neighbour))
    return dist,parent


def shortest_path(parent,start_node,target_node):
    path =[]
    while target_node is not None:
        path.append(target_node)
        target_node = parent[target_node]
        path.reverse()
    return path if path[0] == start_node else []

graph={
    'A':[('B',4),('C',2)],
    'B':[('C',5),('D',10)],
    'C':[('E',3)],
    'D':[],
    'E':[('D',4)]
}


start_node = 'A'
target_node = 'D'

dist,parent = dijistra(graph,start_node)
path = shortest_path(parent,start_node,target_node)

if path:
    print(f"shortest path from {start_node} to {target_node} : {path}")
    print(f"Distance : {dist[target_node]}")
    print(f"Shortest path from {start_node} to {target_node}: {path}")
else:
    print("No shortest path found ")

