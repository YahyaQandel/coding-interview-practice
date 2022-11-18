from unittest import TestCase
from disjoint_set import DisJoingSetQuickFind,DisJoingSetQuickUnion
class TestDisjointSets(TestCase):
    def setUp(self) -> None:
        self.graph_size = 11

    
    def test_connect_quick_find(self):
        self.graph = DisJoingSetQuickFind(self.graph_size)
        self.graph.union(0,1)
        self.graph.union(0,2)
        self.graph.union(1,4)

        self.graph.union(3,7)
        self.graph.union(7,8)

        self.graph.union(5,6)
        self.graph.union(6,9)

        self.assertTrue(self.graph.connected(0,4))
        self.assertTrue(self.graph.connected(3,8))
        self.assertTrue(self.graph.connected(6,5))
        self.assertFalse(self.graph.connected(0,10))


    def test_connect_quick_union(self):
        self.graph = DisJoingSetQuickUnion(self.graph_size)
        self.graph.union(0,1)
        self.graph.union(0,2)
        self.graph.union(1,4)

        self.graph.union(3,7)
        self.graph.union(7,8)

        self.graph.union(5,6)
        self.graph.union(6,9)

        self.assertTrue(self.graph.connected(0,4))
        self.assertTrue(self.graph.connected(3,8))
        self.assertTrue(self.graph.connected(6,5))
        self.assertFalse(self.graph.connected(0,10))

