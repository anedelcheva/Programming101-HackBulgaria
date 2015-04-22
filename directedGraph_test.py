from directedGraph import DirectedGraph
from directedGraph import NoSuchPerson
import unittest


class DirectedGraphTest(unittest.TestCase):

    def setUp(self):
        self.graph1 = DirectedGraph()
        self.graph2 = DirectedGraph()
        self.graph2.add_edge("Aneta", "Tsvety")
        self.graph2.add_edge("Tsvety", "Aneta")
        self.graph2.add_edge("Tsvety", "Krisi")

    def test_init(self):
        self.assertTrue(isinstance(self.graph1, DirectedGraph))

    def test_add_node(self):
        self.graph1.add_edge("Aneta", "Tsvety")
        self.assertEqual(self.graph1.graph, {'Tsvety': [], 'Aneta': ['Tsvety']})
        self.graph1.add_edge("Tsvety", "Aneta")
        self.graph1.add_edge("Tsvety", "Krisi")
        relationships = {
        'Aneta': ['Tsvety'],
        'Tsvety': ['Aneta', 'Krisi'],
        'Krisi': []
        }
        self.assertEqual(self.graph1.graph, relationships)

    def test_get_neighbours_for(self):
        self.assertEqual(self.graph2.get_neighbours_for('Aneta'), ['Tsvety'])
        self.assertEqual(self.graph2.get_neighbours_for('Tsvety'), ['Aneta', 'Krisi'])
        self.assertEqual(self.graph2.get_neighbours_for('Krisi'), [])
        with self.assertRaises(NoSuchPerson):
            self.graph2.get_neighbours_for('Martin')

if __name__ == '__main__':
    unittest.main()
