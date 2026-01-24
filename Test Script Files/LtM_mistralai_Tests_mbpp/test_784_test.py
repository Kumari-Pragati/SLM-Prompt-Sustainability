import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_simple_even_and_odd(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5]), 20)
        self.assertEqual(mul_even_odd([0, 1, 2, 3]), 0)
        self.assertEqual(mul_even_odd([-2, -1, 0, 1]), 2)

    def test_single_even_or_odd(self):
        self.assertEqual(mul_even_odd([2]), 2)
        self.assertEqual(mul_even_odd([1]), 1)
        self.assertEqual(mul_even_odd([0]), -1)

    def test_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), -1)

    def test_all_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)
