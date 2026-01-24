import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_sorted_models(self):
        models = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'blue', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'},
        ]
        expected_result = [
            {'color': 'blue', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'},
            {'color': 'red', 'name': 'model1'},
        ]
        self.assertEqual(sorted_models(models), expected_result)

    def test_sorted_models_with_same_color(self):
        models = [
            {'color': 'red', 'name': 'model1'},
            {'color': 'red', 'name': 'model2'},
            {'color': 'green', 'name': 'model3'},
        ]
        expected_result = [
            {'color': 'green', 'name': 'model3'},
            {'color': 'red', 'name': 'model1'},
            {'color': 'red', 'name': 'model2'},
        ]
        self.assertEqual(sorted_models(models), expected_result)

    def test_sorted_models_with_empty_list(self):
        models = []
        expected_result = []
        self.assertEqual(sorted_models(models), expected_result)
