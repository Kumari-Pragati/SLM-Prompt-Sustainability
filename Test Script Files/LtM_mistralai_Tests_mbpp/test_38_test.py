import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_simple_even_and_odd(self):
        self.assertAlmostEqual(div_even_odd([2, 3, 4, 5]), 2.0)
        self.assertAlmostEqual(div_even_odd([-2, -3, -4, -5]), -2.0)
        self.assertAlmostEqual(div_even_odd([0, 1, 2, 3]), 0.0)

    def test_single_even_or_odd(self):
        self.assertAlmostEqual(div_even_odd([2]), 2.0)
        self.assertAlmostEqual(div_even_odd([1]), 1.0)
        self.assertAlmostEqual(div_even_odd([0]), nan)

    def test_empty_list(self):
        self.assertRaises(StopIteration, div_even_odd, [])

    def test_all_even_or_odd(self):
        self.assertAlmostEqual(div_even_odd([2, 2, 2]), nan)
        self.assertAlmostEqual(div_even_odd([3, 3, 3]), nan)
