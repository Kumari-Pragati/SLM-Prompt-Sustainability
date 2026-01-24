import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(mul_even_odd([]), -1)

    def test_single_even_number(self):
        self.assertIs(mul_even_odd([2]), -1)

    def test_single_odd_number(self):
        self.assertIs(mul_even_odd([3]), -1)

    def test_single_number(self):
        self.assertIs(mul_even_odd([4]), -1)

    def test_mixed_list(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5, 6]), 2 * 3)

    def test_duplicate_even_odd(self):
        self.assertEqual(mul_even_odd([2, 2, 3, 3]), 2 * 3)

    def test_duplicate_even(self):
        self.assertEqual(mul_even_odd([2, 2, 2, 3]), -1)

    def test_duplicate_odd(self):
        self.assertEqual(mul_even_odd([3, 3, 2, 4]), -1)

    def test_all_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), -1)

    def test_all_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)
