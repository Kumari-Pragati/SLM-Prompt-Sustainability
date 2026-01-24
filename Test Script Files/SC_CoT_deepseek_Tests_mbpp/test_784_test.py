import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4]), 8)

    def test_single_even(self):
        self.assertEqual(mul_even_odd([2]), -1)

    def test_single_odd(self):
        self.assertEqual(mul_even_odd([1]), -1)

    def test_no_numbers(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), 24)

    def test_all_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(mul_even_odd([-1, -2, -3, -4]), 8)

    def test_mixed_numbers(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4, 5]), 10)

    def test_large_numbers(self):
        self.assertEqual(mul_even_odd([1000000000, 2000000000, 3]), 6000000000)
