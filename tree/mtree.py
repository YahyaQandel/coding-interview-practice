from collections import deque
from itertools import count
from statistics import mode
from node import Node
class Tree():
    def __init__(self,root) -> None:
        """
        """
        self.root = root
        self.array_rep = []


class DFSTree(Tree):

    def pre_order_traverse(self):
        def pr_o_t(root,array_rep):
            if not root:
                return
            array_rep.append(root)
            pr_o_t(root.left,array_rep)
            pr_o_t(root.right,array_rep)

        pr_o_t(self.root,self.array_rep)


    def post_order_traverse(self):
        def po_o_t(root,array_rep):
            if not root:
                return
            po_o_t(root.left,array_rep)
            po_o_t(root.right,array_rep)
            array_rep.append(root)

        po_o_t(self.root,self.array_rep)

    def in_order_traverse(self):
        def i_o_t(root,array_rep):
            if not root:
                return
            i_o_t(root.left,array_rep)
            array_rep.append(root)
            i_o_t(root.right,array_rep)

        i_o_t(self.root,self.array_rep)


class BFSTree(Tree):

    def traverse(self):
        queue = deque([self.root])
        while len(queue):
            root = queue.popleft()
            self.array_rep.append(root)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        

class BSTree:
    
    def __init__(self):
        self.root = None
    

    def insert(self,value):
        def _add_to(node):
            if not node:
                return Node(value)
            if node.value > value:
                node.left = _add_to(node.left)
            elif node.value < value :
                node.right = _add_to(node.right)
            return node
        self.root = _add_to(self.root)
            
    def nodes_count(self):
        return self._count(self.root)
    
    def _count(self,node):
        if not node:
            return 0
        left_count = self._count(node.left)
        right_count = self._count(node.right)
        return left_count + right_count + 1


    def is_in_tree(self,value):
        def traverse(node):
            if node:
                if node.value == value:
                    return True
                return traverse(node.left) or traverse(node.right)
            return False
        
        return traverse(self.root)

    def _get_lowest_node_value_of_branch(self,node):
        if node.left:
            return self._get_lowest_node_value_of_branch(node.left)
        return node.value

    def delete(self,value):
        def _delete(node,value):
            if node:
                if node.value == value and node.left and node.right:
                    node.value = self._get_lowest_node_value_of_branch(node.right)
                    node.right = _delete(node.right,node.value)  # perform leaf delete
                if node.value == value and node.left == None and node.right == None: # delete a leaf
                    return None 
                if node.value == value and node.left is not None:  # one child left
                    return node.left
                if node.value == value and node.right is not None: # one child right
                    return node.right
                node.left = _delete(node.left,value)
                node.right = _delete(node.right,value)
                return node
        self.root = _delete(self.root,value)


    
    def get_height(self):
        def _height(node):
            if node:
                lheight = _height(node.left) + 1
                rheight = _height(node.right) + 1
                return max(lheight,rheight)
            return 0
        return _height(self.root)
    
    def delete_tree(self):
        self.root = None  # not a good option as we don't have garbage collector to remove other nodes
                          # without closing the app
    
    def get_min(self):
        '''this version is working on a balanced tree
        '''
        if not self.root:
            return None

        if self.root.left:
            return self._get_lowest_node_value_of_branch(self.root.left)
        return self.root.value

    def get_min_unbalanced(self):
        '''this will loop throough all tree items
        '''
        def _min(node):
            if not node:
                return 10000000000000
            left_min = min(_min(node.left),node.value)
            right_min = min(_min(node.right),node.value)
            return min(left_min,right_min)
        return _min(self.root)

    def get_max(self):
        '''this version is working on a balanced tree
        '''
        if not self.root:
            return None

        def _max(node):
            if not node.right:
                return node.value
            return _max(node.right)
        
        return _max(self.root)


    def get_max_unbalanced(self):
        '''this will loop throough all tree items
        '''
        def _max(node):
            if not node:
                return -10000000000000
            left_min = max(_max(node.left),node.value)
            right_min = max(_max(node.right),node.value)
            return max(left_min,right_min)
        return _max(self.root)
    

    def get_successor(self,value):
        '''successor in binary search tree by traversing the tree
        in order'''

        def inorder(node,sorted_tree_as_list,value_index):
            if not node:
                return None
            left = inorder(node.left,sorted_tree_as_list,value_index)
            sorted_tree_as_list.append(node.value)
            if node.value == value:
                value_index = len(sorted_tree_as_list)
            right = inorder(node.right,sorted_tree_as_list,value_index)
            return value_index or left or right
        sorted_tree_as_list = []
        value_index = inorder(self.root,sorted_tree_as_list,0)
        if not value_index:
            return -1
        return sorted_tree_as_list[value_index]

    
    def get_parent(self,value):
        '''we can get parent by traversing inorder'''
        def _parent(node,parent):
            if not node:
                return None
            left_parent = _parent(node.left,node)
            if node.value == value:
                return parent
            right_parent = _parent(node.right,node)
            return left_parent or right_parent
        return _parent(self.root,None)


    
    def print_values(self):
        '''uses inorder traversal to create a sorted list of a tree'''
        def inorder(node,sorted_tree_as_list):
            if not node:
                return None
            left = inorder(node.left,sorted_tree_as_list,)
            sorted_tree_as_list.append(node.value)
            right = inorder(node.right,sorted_tree_as_list)
        sorted_tree_as_list = []
        inorder(self.root,sorted_tree_as_list)
        return sorted_tree_as_list
