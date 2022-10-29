import unittest
from mergesort import MergeSort

class TestMergeSort(unittest.TestCase):
    def setUp(self) -> None:
        self.algo = MergeSort()

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