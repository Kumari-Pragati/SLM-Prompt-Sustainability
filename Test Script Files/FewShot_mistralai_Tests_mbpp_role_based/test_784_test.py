import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5, 6]), 20)
        self.assertEqual(mul_even_odd([4, 5, 6]), 120)
        self.assertEqual(mul_even_odd([2, 4, 6]), 48)

    def test_empty_list(self):
        self.assertIs(mul_even_odd([]), -1)

    def test_single_even_or_odd(self):
        self.assertIs(mul_even_odd([2]), -1)
        self.assertIs(mul_even_odd([3]), -1)

    def test_single_even_and_odd(self):
        self.assertIs(mul_even_odd([2, 3]), -1)

    def test_all_even(self):
        self.assertIs(mul_even_odd([2, 4, 6, 8]), -1)

    def test_all_odd(self):
        self.assertIs(mul_even_odd([1, 3, 5, 7]), -1)
