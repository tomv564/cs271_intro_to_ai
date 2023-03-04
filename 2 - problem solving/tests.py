import unittest
import search


class GraphSearchTests(unittest.TestCase):

    def setUp(self):
        self.graph = {'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
                      'Zerind': ['Oradea'],
                      'Oradea': ['Sibiu'],
                      'Sibiu': ['Fagaras', 'Rimnicu Vilcea'],
                      'Timisoara': ['Lugoj'],
                      'Lugoj': ['Mehadia'],
                      'Mehadia': ['Drobeta'],
                      'Drobeta': ['Craiova'],
                      'Craiova': ['Rimnicu Vilcea', 'Pitesti'],
                      'Rimnicu Vilcea': ['Pitesti', 'Craiova'],
                      'Pitesti': ['Bucharest'],
                      'Fagaras': ['Bucharest'],
                      'Bucharest': ['Urziceni']}

    def test_initialnotfound(self):
        path = search.depth_first_search(self.graph, 'Bananas', 'Sibiu')
        self.assertEqual(None, path)

    def test_alreadythere(self):
        path = search.depth_first_search(self.graph, "Arad", "Arad")
        self.assertEqual(path, ["Arad"])

    def test_firstpath(self):
        path = search.depth_first_search(self.graph, "Arad", "Zerind")
        self.assertEqual(["Arad", "Zerind"], path)

    def test_secondpath(self):
        path = search.depth_first_search(self.graph, "Arad", "Fagaras")
        print(path)
        self.assertEqual(3, len(path))

    def test_alltheway(self):
        path = search.depth_first_search(self.graph, "Arad", "Bucharest")
        print(path)
        self.assertEqual(4, len(path))

    def test_fromhalfway(self):
        path = search.depth_first_search(self.graph, "Sibiu", "Bucharest")
        print(path)
        self.assertEqual(3, len(path))

    def test_breadthfirst(self):
        path = search.breadth_first_search(self.graph, "Arad", "Zerind")
        self.assertEqual(["Arad", "Zerind"], path)


if __name__ == '__main__':
    unittest.main()
