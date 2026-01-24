import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(div_even_odd([2, 3, 4, 5]), 2/3)

    def test_only_even(self):
        self.assertEqual(div_even_odd([2, 4, 6]), -1)

    def test_only_odd(self):
        self.assertEqual(div_even_odd([1, 3, 5]), -1)

    def test_empty_list(self):
        self.assertEqual(div_even_odd([]), -1)

    def test_large_numbers(self):
        self.assertAlmostEqual(div_even_odd([1000000000, 999999999, 888888888, 777777777]), 1000000000/999999999)

    def test_negative_numbers(self):
        self.assertAlmostEqual(div_even_odd([-2, -1, 0, 1, 2]), -2/-1)

    def test_zero(self):
        self.assertEqual(div_even_odd([0, 0, 0]), -1)
