import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_sorts_prices_in_descending_order(self):
        prices = [('1.5', 1.5), ('2.0', 2.0), ('0.5', 0.5)]
        self.assertEqual(float_sort(prices), [('2.0', 2.0), ('1.5', 1.5), ('0.5', 0.5)])

    def test_empty_list(self):
        self.assertEqual(float_sort([]), [])

    def test_single_item(self):
        self.assertEqual(float_sort([('1.0', 1.0)]), [('1.0', 1.0)])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            float_sort([('a', 1.0)])
