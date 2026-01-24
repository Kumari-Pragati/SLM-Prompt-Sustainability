import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(re_arrange([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_simple_negative(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])

    def test_edge_empty(self):
        self.assertEqual(re_arrange([], 0), [])

    def test_edge_single(self):
        self.assertEqual(re_arrange([1], 1), [1])

    def test_edge_zero(self):
        self.assertEqual(re_arrange([0], 1), [0])

    def test_edge_negative(self):
        self.assertEqual(re_arrange([-1], 1), [-1])

    def test_edge_mixed(self):
        self.assertEqual(re_arrange([1, -2, 3, -4, 5], 5), [1, -2, 3, -4, 5])

    def test_complex_positive(self):
        self.assertEqual(re_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_complex_negative(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 10), [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            re_arrange("hello", 5)
