import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_simple_input(self):
        price = [('item1', '10.5'), ('item2', '20.3'), ('item3', '30.7')]
        expected_output = [('item3', '30.7'), ('item2', '20.3'), ('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_empty_input(self):
        price = []
        expected_output = []
        self.assertEqual(float_sort(price), expected_output)

    def test_single_item_input(self):
        price = [('item1', '10.5')]
        expected_output = [('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_same_price_items(self):
        price = [('item1', '10.5'), ('item2', '10.5'), ('item3', '10.5')]
        expected_output = [('item3', '10.5'), ('item2', '10.5'), ('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_negative_prices(self):
        price = [('item1', '-10.5'), ('item2', '-20.3'), ('item3', '-30.7')]
        expected_output = [('item3', '-30.7'), ('item2', '-20.3'), ('item1', '-10.5')]
        self.assertEqual(float_sort(price), expected_output)
