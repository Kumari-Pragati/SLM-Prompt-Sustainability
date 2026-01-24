import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_single_even(self):
        self.assertEqual(mul_even_odd([2, 3, 4]), 6)

    def test_single_odd(self):
        self.assertEqual(mul_even_odd([1, 2, 3]), -1)

    def test_multiple_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), 12)

    def test_multiple_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)

    def test_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_list_with_no_evens(self):
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)

    def test_list_with_no_odds(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), -1)
