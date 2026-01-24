import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5, 6]), 24)
        self.assertEqual(mul_even_odd([-2, -3, 4, 5, -6]), 24)
        self.assertEqual(mul_even_odd([1, 2, 3, 4, 5]), -120)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(mul_even_odd([]), -1)
        self.assertEqual(mul_even_odd([2]), 2)
        self.assertEqual(mul_even_odd([2, 2]), 4)
        self.assertEqual(mul_even_odd([-2, -2]), 4)
        self.assertEqual(mul_even_odd([2, 2, 2]), -4)
        self.assertEqual(mul_even_odd([-2, -2, -2]), -4)

    def test_special_cases(self):
        self.assertEqual(mul_even_odd([0]), 0)
        self.assertEqual(mul_even_odd([2, 2, 2, 2]), 0)
        self.assertEqual(mul_even_odd([-2, -2, -2, -2]), 0)
