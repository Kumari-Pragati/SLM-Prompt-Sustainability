import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_multiply_list_simple(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)
        self.assertEqual(multiply_list([2, 2]), 4)

    def test_multiply_list_edge(self):
        self.assertEqual(multiply_list([0]), 0)
        self.assertEqual(multiply_list([1]), 1)
        self.assertEqual(multiply_list([]), 1)

    def test_multiply_list_boundary(self):
        self.assertEqual(multiply_list([float('inf')]), float('inf'))
        self.assertEqual(multiply_list([float('-inf')]), float('-inf'))
        self.assertEqual(multiply_list([0, float('inf')]), 0)
        self.assertEqual(multiply_list([float('-inf'), 0]), 0)

    def test_multiply_list_complex(self):
        self.assertEqual(multiply_list([1, 2, 3, 4, 5]), 120)
        self.assertEqual(multiply_list([-1, -2, -3]), -6)
        self.assertEqual(multiply_list([2, 0, 2]), 0)
