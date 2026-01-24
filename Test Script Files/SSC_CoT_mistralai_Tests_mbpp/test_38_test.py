import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(div_even_odd([2, 3, 4, 5]), 4.0)
        self.assertAlmostEqual(div_even_odd([-2, -3, 4, 5]), -4.0)
        self.assertAlmostEqual(div_even_odd([2, 3, -4, 5]), -2.0)
        self.assertAlmostEqual(div_even_odd([2, 3, 4, -5]), 0.5)

    def test_edge_cases(self):
        self.assertEqual(div_even_odd([]), None)
        self.assertAlmostEqual(div_even_odd([2]), None)
        self.assertAlmostEqual(div_even_odd([3]), None)
        self.assertAlmostEqual(div_even_odd([0]), None)
        self.assertAlmostEqual(div_even_odd([1]), None)

    def test_boundary_cases(self):
        self.assertAlmostEqual(div_even_odd([-2, 1]), -2.0)
        self.assertAlmostEqual(div_even_odd([2, -1]), 2.0)
        self.assertAlmostEqual(div_even_odd([-2, -1]), -2.0)
        self.assertAlmostEqual(div_even_odd([2, 1]), 0.5)
