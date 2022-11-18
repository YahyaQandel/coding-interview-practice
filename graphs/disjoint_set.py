class DisJoingSetQuickFind():
    def __init__(self,size):
        self.root = [ i for i in range(0,size) ]
    

    def find_root(self,el):
        return self.root[el]
    
    def union(self,first_el,second_el):
        root_first_el = self.find_root(first_el)
        root_second_el = self.find_root(second_el)
        if root_first_el != root_second_el:
            # we will consider first_el is parent
            for el in range(0,len(self.root)):
                if self.find_root(el) == root_second_el:
                    self.root[el] = root_first_el

    def connected(self,first_el,second_el):
        return self.find_root(first_el) == self.find_root(second_el)




class DisJoingSetQuickUnion():
    def __init__(self,size):
        self.root = [ i for i in range(0,size) ]
    

    def find_root(self,el):
        while el != self.root[el]:
            el = self.root[el]
        return el
    
    def union(self,first_el,second_el):
        root_first_el = self.find_root(first_el)
        root_second_el = self.find_root(second_el)
        # we will consider first_el is parent
        if root_first_el != root_second_el:
            self.root[second_el] = first_el

    def connected(self,first_el,second_el):
        return self.find_root(first_el) == self.find_root(second_el)