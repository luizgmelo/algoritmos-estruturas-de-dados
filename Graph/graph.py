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

    # depth first search
    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def traverse(self, v):
        visited = set()

        self.dfs(v, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.traverse("A")
