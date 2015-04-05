# # Implementing the graph traversal Depth First Search using the stack data structure
# # Idea of the algorithm:
# We begin from a node called start. We traverse while we find the desired node end.
# We push the node start onto the stack and mark it as visited. If it is the node we
# are looking for we return true as we have found it. If this is not the case, we begin
# traversing one of its neighbours-push it onto the stack and mark it as visited. Then we
# push one of its neighbours, mark it as visited and so on. If there is nowhere to go,
# we pop a node from the stack and look whether it has neighbours we haven't marked as
# visited. If there is a neighbour which is not marked as visited, we mark it as visited and
# we push it onto the stack. If the current node doesn't have any unvisited nodes we pop it
# from the stack and repeat the same procedure for the element on top of stack while the
# stack is not empty


def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    while len(stack) != 0:
        current_node = stack.pop()
        # if current_node == end:
        #     return True
        if current_node not in visited:
            visited.append(current_node)
            for neighbour in graph[current_node]:
                stack.append(neighbour)
    return visited
    #return False

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

print (dfs(graph, 1))
