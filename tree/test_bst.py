from unittest import TestCase
from mtree import BSTree
from node import Node

class BinarySearchTest(TestCase):
    def setUp(self) -> None:
        self.bstree = BSTree()

    def test_insert_node_in_empty_tree(self):
        self.bstree.insert(10)
        self.assertEqual(self.bstree.root.value,10)

    def test_insert_node_to_left(self):
        left_node_to_root = Node(7)
        right_node_to_root = Node(12)
        root_node = Node(10,left_node_to_root,right_node_to_root) 
        self.bstree.root = root_node
        self.bstree.insert(2)
        self.assertEqual(self.bstree.root.left.left.value,2)

    
    def test_insert_node_to_right(self):
        left_node_to_root = Node(7)
        right_node_to_root = Node(12)
        root_node = Node(10,left_node_to_root,right_node_to_root) 
        self.bstree.root = root_node
        self.bstree.insert(20)
        self.assertEqual(self.bstree.root.right.right.value,20)

    def test_get_nodes_count(self):
        self.bstree.insert(10)
        self.bstree.insert(2)
        self.bstree.insert(4)
        self.bstree.insert(18)
        self.bstree.insert(13)
        self.bstree.insert(20)
        self.bstree.insert(30)
        self.bstree.insert(25)
        self.assertEqual(self.bstree.nodes_count(),8)


    def test_item_is_in_tree(self):
        self.bstree.insert(10)
        self.bstree.insert(2)
        self.bstree.insert(4)
        self.bstree.insert(18)
        self.bstree.insert(13)
        self.bstree.insert(20)
        self.bstree.insert(30)
        self.bstree.insert(25)
        self.assertTrue(self.bstree.is_in_tree(30))
        self.assertFalse(self.bstree.is_in_tree(33))