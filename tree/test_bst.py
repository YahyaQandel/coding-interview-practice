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

    def test_item_is_in_tree_root(self):
        self.bstree.insert(10)
        self.assertTrue(self.bstree.is_in_tree(10))
        self.assertFalse(self.bstree.is_in_tree(33))

    
    def test_delete_leaf_node(self):
        self.bstree.insert(10)
        self.bstree.insert(2)
        self.bstree.insert(4)
        self.bstree.delete(4)
        self.assertFalse(self.bstree.is_in_tree(4))
        self.assertEqual(self.bstree.root.left.value,2)


    def test_delete_one_child_node_left(self):
        self.bstree.insert(10)
        self.bstree.insert(2)
        self.bstree.insert(4)
        self.bstree.delete(2)
        self.assertFalse(self.bstree.is_in_tree(2))
        self.assertEqual(self.bstree.root.left.value,4)
    
    def test_delete_one_child_node_right(self):
        self.bstree.insert(10)
        self.bstree.insert(15)
        self.bstree.insert(18)
        self.bstree.delete(15)
        self.assertFalse(self.bstree.is_in_tree(15))
        self.assertEqual(self.bstree.root.right.value,18)


    def test_delete_two_children_node(self):
        self.bstree.insert(5)
        self.bstree.insert(20)
        self.bstree.insert(10)
        self.bstree.insert(30)
        self.bstree.insert(25)
        self.bstree.insert(35)
        self.bstree.insert(22)
        self.bstree.delete(20)
        self.assertFalse(self.bstree.is_in_tree(20))
        self.assertEqual(self.bstree.root.right.value,22)
        self.assertEqual(self.bstree.root.right.value,22)
        self.assertEqual(self.bstree.root.right.right.value,30)
        self.assertEqual(self.bstree.root.right.right.left.value,25)
        self.assertEqual(self.bstree.root.right.right.right.value,35)
        self.bstree.delete(22)
        self.assertFalse(self.bstree.is_in_tree(22))
        self.assertEqual(self.bstree.root.right.value,25)
        self.assertEqual(self.bstree.root.right.right.value,30)
        self.assertIsNone(self.bstree.root.right.right.left)
        self.assertIsNone(self.bstree.root.right.right.right.left)
        self.bstree.delete(25)
        self.assertEqual(self.bstree.nodes_count(),4)
        self.assertEqual(self.bstree.root.right.value,30)
        self.assertEqual(self.bstree.root.right.left.value,10)
        self.assertEqual(self.bstree.root.right.right.value,35)


    
    def test_get_height(self):
        self.bstree.insert(10)
        self.assertEqual(self.bstree.get_height(),1)
        self.bstree.insert(5)
        self.bstree.insert(4)
        self.bstree.insert(2)
        self.assertEqual(self.bstree.get_height(),4)