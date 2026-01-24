import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_normal_input(self):
        models = [{'name': 'Car1', 'color': 'Red'},
                   {'name': 'Car2', 'color': 'Blue'},
                   {'name': 'Car3', 'color': 'Red'}]
        result = sorted_models(models)
        expected = [{'name': 'Car1', 'color': 'Red'},
                    {'name': 'Car2', 'color': 'Blue'},
                    {'name': 'Car3', 'color': 'Red'}]
        self.assertEqual(result, expected)

    def test_edge_input_same_color(self):
        models = [{'name': 'Car1', 'color': 'Red'},
                   {'name': 'Car2', 'color': 'Red'},
                   {'name': 'Car3', 'color': 'Red'}]
        result = sorted_models(models)
        expected = [{'name': 'Car1', 'color': 'Red'},
                    {'name': 'Car2', 'color': 'Red'},
                    {'name': 'Car3', 'color': 'Red'}]
        self.assertEqual(result, expected)

    def test_edge_input_different_colors(self):
        models = [{'name': 'Car1', 'color': 'Red'},
                   {'name': 'Car2', 'color': 'Blue'},
                   {'name': 'Car3', 'color': 'Green'}]
        result = sorted_models(models)
        expected = [{'name': 'Car1', 'color': 'Red'},
                    {'name': 'Car2', 'color': 'Blue'},
                    {'name': 'Car3', 'color': 'Green'}]
        self.assertEqual(result, expected)

    def test_edge_input_empty(self):
        models = []
        result = sorted_models(models)
        expected = []
        self.assertEqual(result, expected)

    def test_edge_input_single_item(self):
        models = [{'name': 'Car1', 'color': 'Red'}]
        result = sorted_models(models)
        expected = [{'name': 'Car1', 'color': 'Red'}]
        self.assertEqual(result, expected)

    def test_invalid_input_no_color(self):
        models = [{'name': 'Car1'}]
        with self.assertRaises(ValueError):
            sorted_models(models)
