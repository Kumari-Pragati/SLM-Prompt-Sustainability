import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertIs(mul_even_odd([]), -1)

    def test_all_even(self):
        self.assertIs(mul_even_odd([2, 4, 6]), -1)

    def test_all_odd(self):
        self.assertIs(mul_even_odd([1, 3, 5]), -1)

    def test_single_even(self):
        self.assertEqual(mul_even_odd([2]), 2)

    def test_single_odd(self):
        self.assertEqual(mul_even_odd([1]), -1)

    def test_mixed_list(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4]), 2)
