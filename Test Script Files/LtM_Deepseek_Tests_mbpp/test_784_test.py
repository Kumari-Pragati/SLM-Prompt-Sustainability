import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4]), 8)
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), 0)
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)

    def test_edge_conditions(self):
        self.assertEqual(mul_even_odd([]), -1)
        self.assertEqual(mul_even_odd([1]), -1)
        self.assertEqual(mul_even_odd([2]), 4)
        self.assertEqual(mul_even_odd([1, 3, 5, 7, 9]), -1)

    def test_complex_cases(self):
        self.assertEqual(mul_even_odd([10, 15, 20, 25]), 300)
        self.assertEqual(mul_even_odd([1, 3, 5, 7, 9, 11]), -1)
        self.assertEqual(mul_even_odd([2, 4, 6, 8, 10]), 0)
