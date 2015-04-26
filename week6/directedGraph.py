from bfs_with_goal import bfs


class NoSuchPerson(Exception):
    pass


class DirectedGraph:

    def __init__(self):
        self.graph = {}

# this method adds an edge from node_a to node_b
    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.graph[node_a] = [node_b]
        else:
            self.graph[node_a].append(node_b)
        if node_b not in self.graph:
            self.graph[node_b] = []

    def get_neighbours_for(self, node):
        if node not in self.graph:
            raise NoSuchPerson

        return self.graph[node]

    def path_between(self, node_a, node_b):
        return bfs(self.graph, node_a, node_b)
