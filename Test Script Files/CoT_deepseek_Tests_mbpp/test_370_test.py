import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_typical_case(self):
        price = [('item1', '10.5'), ('item2', '20.3'), ('item3', '30.7')]
        expected_output = [('item3', '30.7'), ('item2', '20.3'), ('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_empty_list(self):
        price = []
        expected_output = []
        self.assertEqual(float_sort(price), expected_output)

    def test_single_item(self):
        price = [('item1', '10.5')]
        expected_output = [('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_same_float_values(self):
        price = [('item1', '10.5'), ('item2', '10.5')]
        expected_output = [('item2', '10.5'), ('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_invalid_input(self):
        price = [('item1', '10.5'), ('item2', '20.3'), ('item3', 'invalid')]
        with self.assertRaises(ValueError):
            float_sort(price)
