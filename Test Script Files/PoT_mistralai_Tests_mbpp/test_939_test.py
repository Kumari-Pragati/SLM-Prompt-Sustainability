import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_typical_case(self):
        data = [{'name': 'Car1', 'color': 'red'},
                {'name': 'Car2', 'color': 'blue'},
                {'name': 'Car3', 'color': 'red'}]
        expected = [{'name': 'Car1', 'color': 'red'},
                    {'name': 'Car2', 'color': 'blue'},
                    {'name': 'Car3', 'color': 'red'}]
        self.assertEqual(sorted_models(data), expected)

    def test_edge_case_empty_list(self):
        data = []
        expected = []
        self.assertEqual(sorted_models(data), expected)

    def test_edge_case_single_item(self):
        data = [{'name': 'Car1', 'color': 'red'}]
        expected = [{'name': 'Car1', 'color': 'red'}]
        self.assertEqual(sorted_models(data), expected)

    def test_edge_case_single_item_different_keys(self):
        data = [{'color': 'red'}]
        self.assertRaises(KeyError, sorted_models, data)

    def test_corner_case_different_colors(self):
        data = [{'name': 'Car1', 'color': 'red'},
                {'name': 'Car2', 'color': 'blue'},
                {'name': 'Car3', 'color': 'green'}]
        expected = [{'name': 'Car1', 'color': 'red'},
                    {'name': 'Car2', 'color': 'blue'},
                    {'name': 'Car3', 'color': 'green'}]
        self.assertEqual(sorted_models(data), expected)

    def test_corner_case_same_color(self):
        data = [{'name': 'Car1', 'color': 'red'},
                {'name': 'Car2', 'color': 'red'},
                {'name': 'Car3', 'color': 'red'}]
        expected = [{'name': 'Car1', 'color': 'red'},
                    {'name': 'Car2', 'color': 'red'},
                    {'name': 'Car3', 'color': 'red'}]
        self.assertEqual(sorted_models(data), expected)
