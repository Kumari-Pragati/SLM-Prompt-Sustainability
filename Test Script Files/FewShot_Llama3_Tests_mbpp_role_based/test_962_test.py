import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):
    def test_sum_even_positive_range(self):
        self.assertEqual(sum_Even(1, 10), 25)

    def test_sum_even_negative_range(self):
        self.assertEqual(sum_Even(-5, -1), -5)

    def test_sum_even_zero_range(self):
        self.assertEqual(sum_Even(0, 0), 0)

    def test_sum_even_empty_range(self):
        with self.assertRaises(TypeError):
            sum_Even(1, None)

    def test_sum_even_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_Even("a", 10)
