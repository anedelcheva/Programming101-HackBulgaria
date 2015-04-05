# Breadth First Search graph traversal
# This program checks whether there is a path between 2 nodes start and end

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

graph = {
    1: [2, 5],
    2: [1, 3, 4],
    3: [2, 6],
    4: [2, 5, 6],
    5: [1, 4],
    6: [3, 4],
    7: [8],
    8: [7]
}

print (bfs(graph, 1, 7))
print (bfs(graph, 1, 4))
