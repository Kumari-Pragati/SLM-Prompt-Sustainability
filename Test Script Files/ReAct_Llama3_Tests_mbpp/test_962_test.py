import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_sum_even_typical(self):
        self.assertEqual(sum_Even(1, 10), 25)

    def test_sum_even_edge_lower(self):
        self.assertEqual(sum_Even(1, 1), 0)

    def test_sum_even_edge_upper(self):
        self.assertEqual(sum_Even(1, 2), 1)

    def test_sum_even_edge_lower_equal(self):
        self.assertEqual(sum_Even(1, 1), 0)

    def test_sum_even_edge_upper_equal(self):
        self.assertEqual(sum_Even(1, 2), 1)

    def test_sum_even_negative(self):
        with self.assertRaises(ValueError):
            sum_Even(-1, -10)

    def test_sum_even_non_integer(self):
        with self.assertRaises(TypeError):
            sum_Even(1.5, 10)

    def test_sum_even_lower_greater_than_upper(self):
        with self.assertRaises(ValueError):
            sum_Even(10, 1)
