import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(StopIteration):
            div_even_odd([])

    def test_single_even_number(self):
        self.assertAlmostEqual(div_even_odd([2]), float('nan'))

    def test_single_odd_number(self):
        self.assertAlmostEqual(div_even_odd([1]), float('inf'))

    def test_mixed_list_even_first(self):
        self.assertAlmostEqual(div_even_odd([2, 1]), 2.0)

    def test_mixed_list_odd_first(self):
        self.assertAlmostEqual(div_even_odd([1, 2]), 0.5)

    def test_all_even_numbers(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6]), 1.5)

    def test_all_odd_numbers(self):
        self.assertAlmostEqual(div_even_odd([1, 3, 5]), 0.33333333333333337)

    def test_negative_numbers(self):
        self.assertAlmostEqual(div_even_odd([-2, -1]), 2.0)

    def test_zero(self):
        self.assertAlmostEqual(div_even_odd([0]), float('nan'))
