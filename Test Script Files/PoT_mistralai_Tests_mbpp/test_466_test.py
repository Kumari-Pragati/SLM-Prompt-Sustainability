import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_peak([20, 10, 15, 25, 12]), 2)
        self.assertEqual(find_peak([1, 2, 1, 2, 1]), 3)
        self.assertEqual(find_peak([10, 20, 30, 40, 50]), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_peak([1]), 0)
        self.assertEqual(find_peak([1, 2]), 1)
        self.assertEqual(find_peak([1, 2, 3]), 2)
        self.assertEqual(find_peak([1, 2, 3, 4]), 3)
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6]), 4)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7]), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8]), 7)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)
        self.assertEqual(find_peak([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 9)
        self.assertEqual(find_peak([10, 9, 8, 7, 6, 5, 4, 3]), 8)
        self.assertEqual(find_peak([10, 9, 8, 7, 6, 5]), 6)
        self.assertEqual(find_peak([10, 9, 8, 7]), 7)
        self.assertEqual(find_peak([10, 9]), 9)
        self.assertEqual(find_peak([10]), 10)

    def test_empty_list(self):
        self.assertIsNone(find_peak([]))

    def test_single_element_list(self):
        self.assertEqual(find_peak([1]), 0)

    def test_decreasing_list(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1]), None)

    def test_increasing_and_equal_list(self):
        self.assertEqual(find_peak([1, 1, 1]), None)
        self.assertEqual(find_peak([2, 2, 2]), None)
        self.assertEqual(find_peak([3, 3, 3]), None)
