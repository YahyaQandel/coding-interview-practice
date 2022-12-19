import unittest
from bubblesort import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def setUp(self) -> None:
        self.algo = BubbleSort()

    def test_sort_basic_scenario(self):
        test_arr = [2,6,5,1,7,4,3]
        sorted_test_arr = [1,2,3,4,5,6,7]
        result = self.algo.sort(test_arr)
        self.assertEqual(result, sorted_test_arr)

    def test_sort_basic_scenadrio(self):
        test_arr = [1,2,3,3,2,1,2]
        sorted_test_arr = [1,1,2,2,2,3,3]
        result = self.algo.sort(test_arr)
        self.assertEqual(result, sorted_test_arr)

    def test_one_item(self):
        test_arr = [1]
        sorted_test_arr = [1]
        result = self.algo.sort(test_arr)
        self.assertEqual(result, sorted_test_arr)

    def test_empty_array(self):
        test_arr = []
        sorted_test_arr = []
        result = self.algo.sort(test_arr)
        self.assertEqual(result, sorted_test_arr)

    def test_negative_values(self):
        test_arr = [0,2,-60,51,100,7,4,-3]
        sorted_test_arr = [-60, -3, 0, 2, 4, 7, 51, 100] 
        result = self.algo.sort(test_arr)
        self.assertEqual(result, sorted_test_arr)