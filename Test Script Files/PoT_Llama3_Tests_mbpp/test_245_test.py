import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case(self):
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_boundary_case(self):
        self.assertEqual(max_sum([1, 1, 1, 1, 1], 5), 0)

    def test_corner_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6], 6), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum("abc", 5)

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            max_sum([], 5)

    def test_single_element_input(self):
        self.assertEqual(max_sum([1], 1), 0)

    def test_zero_length_input(self):
        with self.assertRaises(IndexError):
            max_sum([], 0)
