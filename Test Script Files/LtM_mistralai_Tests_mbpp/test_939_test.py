import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_simple_input(self):
        models = [{'name': 'Car1', 'color': 'red'},
                   {'name': 'Car2', 'color': 'blue'},
                   {'name': 'Car3', 'color': 'red'}]
        expected = [{'name': 'Car1', 'color': 'red'},
                    {'name': 'Car2', 'color': 'blue'},
                    {'name': 'Car3', 'color': 'red'}]
        self.assertEqual(sorted_models(models), expected)

    def test_empty_input(self):
        models = []
        self.assertEqual(sorted_models(models), [])

    def test_single_input(self):
        models = [{'name': 'Car', 'color': 'red'}]
        self.assertEqual(sorted_models(models), [{'name': 'Car', 'color': 'red'}])

    def test_duplicate_input(self):
        models = [{'name': 'Car1', 'color': 'red'},
                   {'name': 'Car1', 'color': 'red'},
                   {'name': 'Car2', 'color': 'blue'}]
        expected = [{'name': 'Car1', 'color': 'red'},
                    {'name': 'Car2', 'color': 'blue'}]
        self.assertEqual(sorted_models(models), expected)

    def test_invalid_input(self):
        models = [1, 2, 3]
        self.assertRaises(TypeError, sorted_models, models)

    def test_mixed_input(self):
        models = [{'name': 'Car1', 'color': 'red'},
                   {'name': 'Car2', 'color': 'blue'},
                   {'name': 'Car3', 'color': 1},
                   {'name': 'Car4', 'color': None}]
        expected = [{'name': 'Car1', 'color': 'red'},
                    {'name': 'Car2', 'color': 'blue'},
                    {'name': 'Car3', 'color': None},
                    {'name': 'Car4', 'color': None}]
        self.assertEqual(sorted_models(models), expected)
