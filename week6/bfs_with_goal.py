def bfs(graph, start, end):
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            return True
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return False
