import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_typical_case(self):
        models = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'blue', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'},
        ]
        expected = [
            {'color': 'blue', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'},
            {'color': 'red', 'name': 'model1'},
        ]
        self.assertEqual(sorted_models(models), expected)

    def test_edge_case(self):
        models = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'red', 'name': 'model2'},
            {'color': 'red', 'name': 'model3'},
        ]
        expected = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'red', 'name': 'model2'},
            {'color': 'red', 'name': 'model3'},
        ]
        self.assertEqual(sorted_models(models), expected)

    def test_corner_case(self):
        models = []
        expected = []
        self.assertEqual(sorted_models(models), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sorted_models(123)
