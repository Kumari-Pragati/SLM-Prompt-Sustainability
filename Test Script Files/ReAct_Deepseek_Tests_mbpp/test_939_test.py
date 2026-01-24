import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_typical_case(self):
        models = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'blue', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'}
        ]
        expected_result = [
            {'color': 'blue', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'},
            {'color': 'red', 'name': 'model1'}
        ]
        self.assertEqual(sorted_models(models), expected_result)

    def test_edge_case_same_color(self):
        models = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'red', 'name': 'model2'},
            {'color': 'red', 'name': 'model3'}
        ]
        expected_result = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'red', 'name': 'model2'},
            {'color': 'red', 'name': 'model3'}
        ]
        self.assertEqual(sorted_models(models), expected_result)

    def test_empty_list(self):
        models = []
        expected_result = []
        self.assertEqual(sorted_models(models), expected_result)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            sorted_models(None)
