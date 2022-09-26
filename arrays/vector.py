DEFAULT_CAPACITY = 4

class Vector():
    def __init__(self):
        self._arr = [0] * DEFAULT_CAPACITY
        self._capacity = DEFAULT_CAPACITY
        self._size = 0

    def _extend(self):
        return self._capacity * 2

    def _shrink(self):
        self._capacity /= 2

    def _expand_arr(self):
        self._capacity = self._extend()
        new_arr = [0] * self._capacity
        for i in range(len(self._arr)):
            new_arr[i] = self._arr[i]
        self._arr = new_arr        

    def _shift_right_at_index(self,index):
        for i in range(self._size, index, -1):
            self._arr[i] = self._arr[i - 1]

    def _shift_left_to_index(self,index):
        for i in range(index,self._size - 1):
            self._arr[i] = self._arr[i + 1]
            
    def size(self):
        """return number of items.
        """
        return self._size

    def capacity(self):
        """return number of items it can hold
        """
        return self._capacity

    def is_empty(self):
        """return True if array is empty and False otherwise
        """
        return True if self._size == 0 else False

    def at_index(self,index):
        """returns item at given index, blows up if index out of bounds
        """ 
        if index < 0 or index > self._capacity - 1:
            raise IndexError("index out of bound")
        return self._arr[index]


    def push(self,value):
        """add new item to array
        """ 
        if self._size == self._capacity:
           self._expand_arr()
        self._arr[self._size] = value
        self._size += 1
        
    
    def insert(self,item,index):
        """push item at specific index
        """ 
        if self._size == self._capacity:
            self._expand_arr()
        self._shift_right_at_index(index)
        self._arr[index] = item

    
    def pop(self):
        """remove from end, return value
        """
        self._size -= 1
        if self._size  == self._capacity / 4:
            self._shrink()
        return self._arr[self._size]

    def delete(self,index):
        """delete item at index, shifting all trailing elements left
        """
        self._shift_left_to_index(index)

        self._size -= 1

    def remove(self,value):
        """looks for value and removes index holding it (even if in multiple places)
        """
        occ = 0
        for i in range(self._size):
            if self._arr[i] == value:
                occ += 1

        for i in range(self._size):
            if self._arr[i] == value:
                self._shift_left_to_index(i)

        self._size -= occ
        
    
    def find(self,value):
        """looks for value and returns first index with that value, -1 if not found
        """
        for i in range(self._size):
            if self._arr[i] == value:
                return i
        return -1