from collections import deque
from itertools import count
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