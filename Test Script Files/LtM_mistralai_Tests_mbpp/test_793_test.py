import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(last([4, 5, 6, 7, 8], 6, 4), 2)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 5), 4)
        self.assertEqual(last([10, 11, 12, 13, 14], 14, 5), 4)

    def test_edge_and_boundary(self):
        self.assertEqual(last([], 10, 0), -1)
        self.assertEqual(last([10], 10, 1), 0)
        self.assertEqual(last([10], 11, 1), -1)
        self.assertEqual(last([10, 10], 10, 2), 1)

    def test_complex(self):
        self.assertEqual(last([1, 3, 5, 6, 7, 8, 9, 10], 6, 8), 4)
        self.assertEqual(last([1, 3, 5, 6, 7, 8, 9, 10], 10, 8), 7)
        self.assertEqual(last([1, 3, 5, 6, 7, 8, 9, 10], 11, 8), -1)
        self.assertEqual(last([1, 3, 5, 6, 7, 8, 9, 10], 0, 8), -1)
