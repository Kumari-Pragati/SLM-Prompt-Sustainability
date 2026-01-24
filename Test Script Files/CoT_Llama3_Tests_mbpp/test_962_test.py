import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):
    def test_sum_even_positive(self):
        self.assertEqual(sum_Even(1, 10), 25)

    def test_sum_even_negative(self):
        with self.assertRaises(ValueError):
            sum_Even(-1, 10)

    def test_sum_even_zero(self):
        self.assertEqual(sum_Even(0, 0), 0)

    def test_sum_even_edge(self):
        self.assertEqual(sum_Even(1, 1), 1)

    def test_sum_even_invalid(self):
        with self.assertRaises(TypeError):
            sum_Even('a', 10)

    def test_sum_even_range(self):
        self.assertEqual(sum_Even(5, 10), 30)
