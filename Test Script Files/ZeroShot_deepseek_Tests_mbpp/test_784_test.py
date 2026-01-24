import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_mul_even_odd(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4]), 8)
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), -1)
        self.assertEqual(mul_even_odd([1]), -1)
        self.assertEqual(mul_even_odd([]), -1)
        self.assertEqual(mul_even_odd([10, 15, 20, 25]), 300)
