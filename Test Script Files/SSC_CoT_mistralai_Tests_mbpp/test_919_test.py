import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)

    def test_edge_cases(self):
        self.assertEqual(multiply_list([0]), 0)
        self.assertEqual(multiply_list([1]), 1)
        self.assertEqual(multiply_list([-1, -2, -3]), 6)

    def test_boundary_cases(self):
        self.assertEqual(multiply_list([float('inf')]), float('inf'))
        self.assertEqual(multiply_list([-float('inf')]), -float('inf'))

    def test_invalid_input(self):
        self.assertRaises(TypeError, multiply_list, [1, 'a', 3])
