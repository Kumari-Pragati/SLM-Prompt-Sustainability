import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_typical_case(self):
        price = [('item1', '12.5'), ('item2', '20.0'), ('item3', '15.75')]
        expected_output = [('item2', '20.0'), ('item3', '15.75'), ('item1', '12.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_empty_list(self):
        price = []
        expected_output = []
        self.assertEqual(float_sort(price), expected_output)

    def test_single_item(self):
        price = [('item1', '10.0')]
        expected_output = [('item1', '10.0')]
        self.assertEqual(float_sort(price), expected_output)

    def test_same_prices(self):
        price = [('item1', '12.5'), ('item2', '12.5'), ('item3', '12.5')]
        expected_output = [('item2', '12.5'), ('item3', '12.5'), ('item1', '12.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_negative_prices(self):
        price = [('item1', '-12.5'), ('item2', '-20.0'), ('item3', '-15.75')]
        expected_output = [('item2', '-20.0'), ('item3', '-15.75'), ('item1', '-12.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_non_numeric_prices(self):
        price = [('item1', 'abc'), ('item2', 'def'), ('item3', 'ghi')]
        with self.assertRaises(ValueError):
            float_sort(price)
