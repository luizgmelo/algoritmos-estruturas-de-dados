# Graph using dictionary and Sets
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = set()

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].add(str(to_node))

    def delete_node(self):
        pass

    def search_node(self):
        pass

    def traverse(self):
        pass

if __name__ == "__main__":
    graph = Graph()
