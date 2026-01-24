import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_typical_case(self):
        price = [('item1', '10.5'), ('item2', '20.3'), ('item3', '30.7')]
        expected_output = [('item3', '30.7'), ('item2', '20.3'), ('item1', '10.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_edge_case_single_item(self):
        price = [('item1', '5.5')]
        expected_output = [('item1', '5.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_edge_case_empty_list(self):
        price = []
        expected_output = []
        self.assertEqual(float_sort(price), expected_output)

    def test_boundary_case_same_prices(self):
        price = [('item1', '20.0'), ('item2', '20.0'), ('item3', '20.0')]
        expected_output = [('item3', '20.0'), ('item2', '20.0'), ('item1', '20.0')]
        self.assertEqual(float_sort(price), expected_output)

    def test_corner_case_negative_prices(self):
        price = [('item1', '-10.5'), ('item2', '-20.3'), ('item3', '-30.7')]
        expected_output = [('item3', '-30.7'), ('item2', '-20.3'), ('item1', '-10.5')]
        self.assertEqual(float_sort(price), expected_output)
