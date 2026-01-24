import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(div_even_odd([2, 3, 4]), 2/3)

    def test_edge_conditions(self):
        self.assertEqual(div_even_odd([1, 3, 5]), -1)
        self.assertEqual(div_even_odd([2]), -1)
        self.assertEqual(div_even_odd([]), -1)

    def test_complex_cases(self):
        self.assertAlmostEqual(div_even_odd([10, 15, 20]), 10/15)
        self.assertAlmostEqual(div_even_odd([-2, -3, -4]), -2/-3)
        self.assertAlmostEqual(div_even_odd([2, 0, 4]), 0)
        self.assertEqual(div_even_odd([1, 3, 5, 7]), -1)
