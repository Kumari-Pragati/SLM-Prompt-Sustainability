import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_simple_input(self):
        models = [
            {'color': 'red'},
            {'color': 'blue'},
            {'color': 'green'}
        ]
        expected_output = [
            {'color': 'blue'},
            {'color': 'green'},
            {'color': 'red'}
        ]
        self.assertEqual(sorted_models(models), expected_output)

    def test_edge_condition_empty_input(self):
        self.assertEqual(sorted_models([]), [])

    def test_edge_condition_single_input(self):
        models = [{'color': 'red'}]
        expected_output = [{'color': 'red'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_complex_input(self):
        models = [
            {'color': 'red'},
            {'color': 'blue'},
            {'color': 'red'},
            {'color': 'green'}
        ]
        expected_output = [
            {'color': 'blue'},
            {'color': 'green'},
            {'color': 'red'},
            {'color': 'red'}
        ]
        self.assertEqual(sorted_models(models), expected_output)
