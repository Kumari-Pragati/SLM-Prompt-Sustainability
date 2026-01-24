import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_edge_condition(self):
        self.assertEqual(mul_list([0], [100]), [0])

    def test_boundary_condition(self):
        self.assertEqual(mul_list([-1, 1], [1, -1]), [-1, 1])

    def test_different_lengths(self):
        self.assertEqual(mul_list([1, 2, 3, 4], [5, 6]), [5, 12, 18])

    def test_empty_lists(self):
        self.assertEqual(mul_list([], []), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], 'not a list')
