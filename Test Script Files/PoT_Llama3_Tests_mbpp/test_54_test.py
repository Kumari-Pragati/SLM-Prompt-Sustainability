import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    def test_edge_case(self):
        self.assertEqual(counting_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_edge_case2(self):
        self.assertEqual(counting_sort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

    def test_edge_case3(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])

    def test_edge_case4(self):
        self.assertEqual(counting_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case5(self):
        self.assertEqual(counting_sort([]), [])

    def test_edge_case6(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_edge_case7(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])
