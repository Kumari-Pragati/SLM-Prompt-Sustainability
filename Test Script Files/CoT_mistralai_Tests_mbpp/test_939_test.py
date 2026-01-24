import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sorted_models([]), [])

    def test_single_item(self):
        data = [{'model': 'Car', 'color': 'Red'}]
        result = sorted_models(data)
        expected = data
        self.assertEqual(result, expected)

    def test_multiple_items_same_color(self):
        data = [{'model': 'Car', 'color': 'Red'}, {'model': 'Truck', 'color': 'Red'}]
        result = sorted_models(data)
        expected = data
        self.assertEqual(result, expected)

    def test_multiple_items_different_colors(self):
        data = [{'model': 'Car', 'color': 'Red'}, {'model': 'Truck', 'color': 'Blue'}]
        result = sorted_models(data)
        expected = [{'model': 'Car', 'color': 'Red'}, {'model': 'Truck', 'color': 'Blue'}]
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sorted_models(123)

    def test_missing_color(self):
        with self.assertRaises(KeyError):
            data = [{'model': 'Car'}]
            sorted_models(data)
