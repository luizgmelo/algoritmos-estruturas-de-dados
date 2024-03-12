import unittest
import graph

class TestGraphMethods(unittest.TestCase):
    def test_add_node(self):
        my_graph = graph.Graph()
        my_graph.add_node("A")
        my_graph.add_node("B")
        my_graph.add_node("C")
        self.assertEqual(my_graph.graph["A"], set())
        self.assertEqual(my_graph.graph["B"], set())
        self.assertEqual(my_graph.graph["C"], set())
        
    def test_add_edge(self):
        my_graph = graph.Graph()
        my_graph.add_edge("A", "B")
        self.assertEqual(my_graph.graph["A"], set("B"))
        self.assertEqual(my_graph.graph["B"], set())
        my_graph.add_edge("A", "B")
        self.assertEqual(my_graph.graph["A"], set("B"))
        self.assertEqual(my_graph.graph["B"], set())

    def test_delete_edge(self):
        my_graph = graph.Graph()
        my_graph.add_edge("A", "B")
        my_graph.delete_edge("A", "B")
        self.assertEqual(my_graph.graph["A"], set())
        self.assertEqual(my_graph.graph["B"], set())

    def test_delete_node(self):
        my_graph = graph.Graph()
        my_graph.add_edge("A", "B")
        my_graph.delete_node("A")
        my_graph.delete_node("B")
        with self.assertRaises(KeyError):
            my_graph.graph["A"]
            my_graph.graph["B"]

    def test_search_node(self):
        my_graph = graph.Graph()
        my_graph.add_edge("A", "B")
        my_graph.add_edge("A", "C")
        my_graph.add_edge("B", "C")
        my_graph.add_edge("C", "D")
        self.assertEqual(my_graph.search_node("A"), True)
        self.assertEqual(my_graph.search_node("B"), True)
        self.assertEqual(my_graph.search_node("C"), True)
        self.assertEqual(my_graph.search_node("D"), True)
        self.assertEqual(my_graph.search_node("E"), False)
        self.assertEqual(my_graph.search_node("F"), False)
        self.assertEqual(my_graph.search_node("G"), False)
        self.assertEqual(my_graph.search_node("H"), False)

    def test_has_path(self):
        my_graph = graph.Graph()
        my_graph.add_edge("A", "B")
        my_graph.add_edge("A", "C")
        my_graph.add_edge("B", "C")
        my_graph.add_edge("C", "D")
        self.assertEqual(my_graph.has_path("A", "B"), True)
        self.assertEqual(my_graph.has_path("A", "C"), True)
        self.assertEqual(my_graph.has_path("A", "D"), True)
        self.assertEqual(my_graph.has_path("B", "A"), False)
        self.assertEqual(my_graph.has_path("B", "C"), True)
        self.assertEqual(my_graph.has_path("B", "D"), True)
        self.assertEqual(my_graph.has_path("C", "B"), False)
        self.assertEqual(my_graph.has_path("C", "D"), True)
        






