import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_sorted_models_empty_list(self):
        self.assertEqual(sorted_models([]), [])

    def test_sorted_models_single_item(self):
        model = {'name': 'Car', 'color': 'Red'}
        self.assertEqual(sorted_models([model]), [model])

    def test_sorted_models_multiple_items_same_color(self):
        models = [
            {'name': 'Car', 'color': 'Red'},
            {'name': 'Bike', 'color': 'Red'},
            {'name': 'Car', 'color': 'Red'}
        ]
        expected = [
            {'name': 'Car', 'color': 'Red'},
            {'name': 'Bike', 'color': 'Red'},
            {'name': 'Car', 'color': 'Red'}
        ]
        self.assertEqual(sorted_models(models), expected)

    def test_sorted_models_multiple_items_different_colors(self):
        models = [
            {'name': 'Car', 'color': 'Red'},
            {'name': 'Bike', 'color': 'Blue'},
            {'name': 'Car', 'color': 'Green'}
        ]
        expected = [
            {'name': 'Car', 'color': 'Green'},
            {'name': 'Car', 'color': 'Red'},
            {'name': 'Bike', 'color': 'Blue'}
        ]
        self.assertEqual(sorted_models(models), expected)

    def test_sorted_models_case_insensitive_color(self):
        models = [
            {'name': 'Car', 'color': 'red'},
            {'name': 'Bike', 'color': 'BLUE'}
        ]
        expected = [
            {'name': 'Car', 'color': 'red'},
            {'name': 'Bike', 'color': 'BLUE'}
        ]
        self.assertEqual(sorted_models(models), expected)

    def test_sorted_models_missing_color(self):
        models = [
            {'name': 'Car', 'color': None},
            {'name': 'Bike', 'color': 'Blue'}
        ]
        self.assertEqual(sorted_models(models), [
            {'name': 'Car', 'color': None},
            {'name': 'Bike', 'color': 'Blue'}
        ])

    def test_sorted_models_invalid_color_type(self):
        models = [
            {'name': 'Car', 'color': 123},
            {'name': 'Bike', 'color': 'Blue'}
        ]
        self.assertEqual(sorted_models(models), [
            {'name': 'Car', 'color': 123},
            {'name': 'Bike', 'color': 'Blue'}
        ])
