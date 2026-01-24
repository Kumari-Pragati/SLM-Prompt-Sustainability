import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):
    def test_sorted_by_color_ascending(self):
        models = [
            {'name': 'Red Car', 'color': 'red'},
            {'name': 'Blue Car', 'color': 'blue'},
            {'name': 'Green Car', 'color': 'green'}
        ]
        sorted_models = sorted_models(models)
        self.assertEqual(sorted_models, [
            {'name': 'Red Car', 'color': 'red'},
            {'name': 'Blue Car', 'color': 'blue'},
            {'name': 'Green Car', 'color': 'green'}
        ])

    def test_empty_list(self):
        self.assertEqual(sorted_models([]), [])

    def test_single_item(self):
        models = [{'name': 'Single Item', 'color': 'red'}]
        sorted_models(models)
        self.assertEqual(models, [{'name': 'Single Item', 'color': 'red'}])

    def test_duplicate_items(self):
        models = [
            {'name': 'Red Car', 'color': 'red'},
            {'name': 'Red Car', 'color': 'red'},
            {'name': 'Blue Car', 'color': 'blue'}
        ]
        sorted_models(models)
        self.assertEqual(models, [
            {'name': 'Red Car', 'color': 'red'},
            {'name': 'Red Car', 'color': 'red'},
            {'name': 'Blue Car', 'color': 'blue'}
        ])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sorted_models(123)
