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

    def delete_edge(self, from_node, to_node):
        self.graph[from_node].discard(to_node)

    def delete_node(self, node_to_delete):
        del self.graph[node_to_delete]

        for node in self.graph:
            self.delete_edge(node, node_to_delete)

    def search_node(self, node):
        if node in self.graph.keys():
            return True
        return False

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

    def has_path(self, from_node, to_node):
        visited = set()

        return self.dfs_check(from_node, to_node, visited)

    def dfs_check(self, start, end, visited):
        if start == end:
            return True
        visited.add(start)

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                if self.dfs_check(neighbour, end, visited):
                    return True
        return False




if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.traverse("A")
    print(graph.has_path("B", "C"))
