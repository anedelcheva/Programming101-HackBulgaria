def bfs(graph, start):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    while len(queue) != 0:
        current_node = queue.pop(0)
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
    return visited

graph = {
    1: [2, 4, 5],
    2: [1, 3, 4],
    3: [2, 6],
    4: [1, 2, 5, 6],
    5: [1, 4],
    6: [3, 4],
    7: [8],
    8: [7]
}

print (bfs(graph, 1))
