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


my_graph = DirectedGraph()
my_graph.add_edge("Aneta", "Ivan")
print (my_graph.graph)
my_graph.add_edge("Aneta", "Anika")
my_graph.add_edge("Anika", "Aneta")
print (my_graph.graph)
my_graph.add_edge("Ivan", "Niki")
print (my_graph.graph)
#print (my_graph.get_neighbours_for("An"))
