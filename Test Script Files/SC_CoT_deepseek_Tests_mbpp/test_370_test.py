import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_typical_case(self):
        price = [('item1', '12.5'), ('item2', '20.0'), ('item3', '15.75')]
        expected_output = [('item2', '20.0'), ('item3', '15.75'), ('item1', '12.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_edge_case(self):
        price = [('item1', '0.0'), ('item2', '0.0')]
        expected_output = [('item2', '0.0'), ('item1', '0.0')]
        self.assertEqual(float_sort(price), expected_output)

    def test_boundary_case(self):
        price = [('item1', '100.0'), ('item2', '100.0')]
        expected_output = [('item1', '100.0'), ('item2', '100.0')]
        self.assertEqual(float_sort(price), expected_output)

    def test_special_case(self):
        price = [('item1', '12.5'), ('item2', '20.0'), ('item3', '15.75'), ('item4', '12.5')]
        expected_output = [('item2', '20.0'), ('item3', '15.75'), ('item1', '12.5'), ('item4', '12.5')]
        self.assertEqual(float_sort(price), expected_output)

    def test_invalid_input(self):
        price = [('item1', '12.5'), ('item2', '20.0'), ('item3', 'abc')]
        with self.assertRaises(ValueError):
            float_sort(price)
