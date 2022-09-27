from collections import deque

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
        