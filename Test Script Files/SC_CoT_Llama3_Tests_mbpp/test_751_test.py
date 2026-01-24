import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(check_min_heap(arr, 0))

    def test_edge_case(self):
        arr = [1, 2, 3, 4]
        self.assertTrue(check_min_heap(arr, 0))

    def test_edge_case2(self):
        arr = [1, 2, 3]
        self.assertTrue(check_min_heap(arr, 0))

    def test_edge_case3(self):
        arr = [1, 2]
        self.assertTrue(check_min_heap(arr, 0))

    def test_edge_case4(self):
        arr = [1]
        self.assertTrue(check_min_heap(arr, 0))

    def test_edge_case5(self):
        arr = []
        self.assertTrue(check_min_heap(arr, 0))

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        with self.assertRaises(IndexError):
            check_min_heap(arr, 20)

    def test_corner_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        self.assertTrue(check_min_heap(arr, 19))

    def test_corner_case2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        self.assertTrue(check_min_heap(arr, 19))
