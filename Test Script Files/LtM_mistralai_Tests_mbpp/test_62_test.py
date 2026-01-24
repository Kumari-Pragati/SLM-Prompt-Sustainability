import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(smallest_num([1, 2, 3]), 1)
        self.assertEqual(smallest_num([-1, -2, -3]), -3)
        self.assertEqual(smallest_num([0, 0, 0]), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(smallest_num([]), None)
        self.assertEqual(smallest_num([float('inf')]), float('inf'))
        self.assertEqual(smallest_num([-float('inf')]), -float('inf'))

    def test_complex_input(self):
        self.assertEqual(smallest_num([-1, 1, -2, 2, -3, 3]), -3)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(smallest_num([1000000000000000000, 1, 2, 3]), 1)
