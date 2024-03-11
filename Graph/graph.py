# Graph using dictionary and Sets
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def delete_node(self):
        pass

    def search_node(self):
        pass

    def traverse(self):
        pass

if __name__ == "__main__":
    graph = Graph()
