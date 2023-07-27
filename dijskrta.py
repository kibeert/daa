import heapq

def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    visited = [False] * num_vertices
    pq = [(0, source)]  # Priority queue to store (distance, vertex) pairs

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if visited[current_vertex]:
            continue

        visited[current_vertex] = True

        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight > 0 and not visited[neighbor]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph represented as an adjacency matrix
graph = [
    [0, 8, 0, 0, 10, 0, 0],
    [8, 0, 3, 2, 5, 0, 0],
    [0, 3, 0, 2, 0, 0, 2],
    [0, 2, 2, 0, 5, 10, 5],
    [10, 0, 0, 5, 0, 13, 9],
    [0, 0, 0, 10, 13, 0, 9],
    [0, 0, 2, 5, 0, 9, 0]
]

source_vertex = 0  # A is the source vertex in the example

shortest_distances = dijkstra(graph, source_vertex)

# Print the shortest distances from the source vertex to all other vertices
print("Shortest Distances from Source Vertex (A):")
for i, distance in enumerate(shortest_distances):
    print(f"Vertex {chr(65 + i)}: {distance}")
