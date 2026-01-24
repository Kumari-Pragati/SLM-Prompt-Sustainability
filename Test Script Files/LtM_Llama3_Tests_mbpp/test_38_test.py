import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_div_even_odd_typical(self):
        self.assertEqual(div_even_odd([2, 3, 4, 5]), 2/3)

    def test_div_even_odd_empty_list(self):
        with self.assertRaises(ValueError):
            div_even_odd([])

    def test_div_even_odd_single_element(self):
        self.assertEqual(div_even_odd([2]), 2/2)

    def test_div_even_odd_no_even(self):
        with self.assertRaises(ValueError):
            div_even_odd([1, 3, 5, 7])

    def test_div_even_odd_no_odd(self):
        with self.assertRaises(ValueError):
            div_even_odd([2, 4, 6, 8])

    def test_div_even_odd_multiple_evens(self):
        self.assertEqual(div_even_odd([2, 4, 6, 8]), 2/8)

    def test_div_even_odd_multiple_odds(self):
        self.assertEqual(div_even_odd([1, 3, 5, 7]), 1/7)

    def test_div_even_odd_mixed(self):
        self.assertEqual(div_even_odd([2, 3, 4, 5]), 2/5)
