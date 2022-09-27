import unittest
from mtree import DFSTree, BFSTree
from node import Node


class TestTree(unittest.TestCase):
    def assert_array_rep(self,expected_arr,actual_arr):
        if len(expected_arr) != len(actual_arr):
            raise ValueError("expected arr not equal actual arr in length")
        for i in range(len(expected_arr)):
            self.assertEqual(
                expected_arr[i],actual_arr[i].value,
                "node #{} expected arr value {} doesnt equal actual arr value {}".format(
                    i,expected_arr[i],
                    actual_arr[i].value
                    )
            )

class TestDFSTree(TestTree):

    def test_traverse_tree_preorder(self):
        left_1 = Node(5,None,None)
        right_1 = Node(10,None,None)
        root = Node(7,left_1,right_1)
        tree = DFSTree(root)
        tree.pre_order_traverse()
        self.assert_array_rep([7,5,10],tree.array_rep)


    def test_traverse_tree_inorder(self):
        left_1 = Node(5,None,None)
        right_1 = Node(10,None,None)
        root = Node(7,left_1,right_1)
        tree = DFSTree(root)
        tree.in_order_traverse()
        self.assert_array_rep([5,7,10],tree.array_rep)

    def test_traverse_tree_postorder(self):
        left_1 = Node(5,None,None)
        right_1 = Node(10,None,None)
        root = Node(7,left_1,right_1)
        tree = DFSTree(root)
        tree.post_order_traverse()
        self.assert_array_rep([5,10,7],tree.array_rep)


    def test_traverse_tree_postorder_multilevel(self):
        left_1_left = Node(1,None,None)
        left_1_right = Node(6,None,None)
        right_1_left = Node(8,None,None)
        right_1_right = Node(12,None,None)
        left_1 = Node(5,left_1_left,left_1_right)
        right_1 = Node(10,right_1_left,right_1_right)
        root = Node(7,left_1,right_1)
        tree = DFSTree(root)
        tree.post_order_traverse()
        self.assert_array_rep([1,6,5,8,12,10,7],tree.array_rep)



class TestBFSTree(TestTree):
    
    def test_traverse(self):
        left_1_left = Node(1,None,None)
        left_1_right = Node(6,None,None)
        right_1_left = Node(8,None,None)
        right_1_right = Node(12,None,None)
        left_1 = Node(5,left_1_left,left_1_right)
        right_1 = Node(10,right_1_left,right_1_right)
        root = Node(7,left_1,right_1)
        tree = BFSTree(root)
        tree.traverse()
        self.assert_array_rep([7,5,10,1,6,8,12],tree.array_rep)
