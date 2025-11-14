import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm for shortest paths from a single source.
    graph: dict[node] = list of (neighbor, weight)
    start: source node
    Returns: dict of shortest distances and paths
    """
    # Initialize distances and parent trackers
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {node: None for node in graph}

    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)

        # Skip if this is not the shortest path to node
        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent


def shortest_path(parent, start, target):
    """Reconstruct shortest path from start to target."""
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1] if path[-1] == start else []


# Example: weighted directed graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [],
    'E': [('D', 4)]
}

# Run Dijkstra
dist, parent = dijkstra(graph, 'A')

print("Shortest distances:")
for node, d in dist.items():
    print(f"A → {node}: {d}")

print("\nShortest paths:")
for node in graph:
    if node != 'A':
        print(f"A → {node}: {shortest_path(parent, 'A', node)}")
