import unittest
from vector import Vector

class VectorTest(unittest.TestCase):
    def setUp(self):
        self.v = Vector()

    def test_size(self):
        self.assertEqual(self.v.size(),0)

    def test_capacity(self):
        self.assertEqual(self.v.capacity(),4)

    def test_is_empty(self):
        self.assertEqual(self.v.is_empty(),True)

    def test_at_index(self):
        self.v.push(9)
        self.v.push(10)
        self.v.push(11)
        self.assertEqual(self.v.at_index(2),11)
        self.assertRaises(IndexError,self.v.at_index,-1)
        self.assertRaises(IndexError,self.v.at_index,5)

    def test_push(self):
        self.v.push(11)
        self.assertEqual(self.v.at_index(0),11)        
        self.v.push(20)
        self.v.push(30)
        self.v.push(40)
        self.v.push(50)
        self.assertEqual(self.v.at_index(4),50)

    def test_push_over_capacity(self):
        self.v.push(11)
        self.v.push(20)
        self.v.push(30)
        self.v.push(40)
        self.v.push(50)
        self.assertEqual(self.v.at_index(4),50)

    def test_insert_item_at_index(self):
        self.v.push(100)
        self.v.push(200)
        self.v.push(300)
        self.v.push(500)
        self.v.push(600)
        self.assertEqual(self.v.at_index(3),500)        
        self.v.insert(400,3)
        self.assertEqual(self.v.at_index(0),100)        
        self.assertEqual(self.v.at_index(1),200)        
        self.assertEqual(self.v.at_index(2),300)        
        self.assertEqual(self.v.at_index(3),400)        
        self.assertEqual(self.v.at_index(4),500)        
        self.assertEqual(self.v.at_index(5),600)        

    def test_pop(self):
        self.v.push(100)
        self.v.push(200)
        self.v.push(300)
        self.assertEqual(self.v.pop(),300)        
        self.assertEqual(self.v.pop(),200)        
        self.assertEqual(self.v.pop(),100)        
        self.assertEqual(self.v.size(),0)        

    def test_delete(self):
        self.v.push(100)
        self.v.push(200)
        self.v.push(300)
        self.v.push(1000)
        self.v.push(400)
        self.assertEqual(self.v.at_index(3),1000)        
        self.v.delete(3)
        self.assertEqual(self.v.at_index(0),100)        
        self.assertEqual(self.v.at_index(1),200)        
        self.assertEqual(self.v.at_index(2),300)        
        self.assertEqual(self.v.at_index(3),400)        
        self.assertEqual(self.v._size,4)

    def test_delete_index_at_beginning(self):
        self.v.push(1000)
        self.v.push(100)
        self.v.push(200)
        self.v.push(300)
        self.v.push(400)
        self.assertEqual(self.v.at_index(0),1000)        
        self.v.delete(0)
        self.assertEqual(self.v.at_index(0),100)        
        self.assertEqual(self.v.at_index(1),200)        
        self.assertEqual(self.v.at_index(2),300)        
        self.assertEqual(self.v.at_index(3),400)  
        self.assertEqual(self.v._size,4)

    def test_delete_index_at_end(self):
        self.v.push(100)
        self.v.push(200)
        self.v.push(300)
        self.v.push(400)
        self.v.push(1000)
        self.assertEqual(self.v.at_index(4),1000)        
        self.v.delete(4)
        self.assertEqual(self.v.at_index(0),100)        
        self.assertEqual(self.v.at_index(1),200)        
        self.assertEqual(self.v.at_index(2),300)        
        self.assertEqual(self.v.at_index(3),400)  
        self.assertEqual(self.v._size,4)

    def test_remove_item(self):
        self.v.push(100)
        self.v.push(300)
        self.v.push(200)
        self.v.push(400)
        self.v.push(500)
        self.v.push(200)
        self.v.push(600)
        self.v.push(200)
        self.v.remove(200)
        self.assertEqual(self.v.at_index(0),100)        
        self.assertEqual(self.v.at_index(1),300)        
        self.assertEqual(self.v.at_index(2),400)  
        self.assertEqual(self.v.at_index(3),500)  
        self.assertEqual(self.v.at_index(4),600)  
        self.assertEqual(self.v._size,5)

    def test_find_item_already_exists(self):
        self.v.push(100)
        self.v.push(200)
        self.v.push(200)
        self.v.push(400)
        self.v.push(200)
        self.assertEqual(self.v.find(200),1)

    def test_find_item_not_exists(self):
        self.v.push(100)
        self.v.push(200)
        self.v.push(200)
        self.v.push(400)
        self.v.push(200)
        self.assertEqual(self.v.find(500),-1)

    # def test_resize_capacity(self):
    #     pass

