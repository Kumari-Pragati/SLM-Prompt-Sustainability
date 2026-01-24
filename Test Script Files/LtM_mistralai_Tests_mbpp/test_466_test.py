import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_peak([20, 10, 25, 15, 20]), 2)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6]), 5)

    def test_edge_and_boundary(self):
        self.assertEqual(find_peak([1]), 0)
        self.assertEqual(find_peak([1, 2]), 1)
        self.assertEqual(find_peak([1, 2, 3]), 2)
        self.assertEqual(find_peak([1, 2, 3, 4]), 3)
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6]), 5)
        self.assertEqual(find_peak([5, 4, 3, 2, 1]), 0)
        self.assertEqual(find_peak([5, 4, 3, 2]), 2)
        self.assertEqual(find_peak([5, 4, 3]), 2)
        self.assertEqual(find_peak([5, 4]), 1)
        self.assertEqual(find_peak([5]), 0)
        self.assertEqual(find_peak([]), None)

    def test_complex(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 4, 3]), 4)
        self.assertEqual(find_peak([1, 2, 2, 2, 2, 1]), 4)
        self.assertEqual(find_peak([1, 1, 2, 1, 1, 2]), 3)
        self.assertEqual(find_peak([1, 1, 1, 2, 1, 1, 1]), 4)
        self.assertEqual(find_peak([1, 1, 1, 1, 2, 1, 1]), 5)
