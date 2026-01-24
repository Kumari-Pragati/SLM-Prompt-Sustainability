import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sorted_models([]), [])

    def test_single_model(self):
        models = [{'color':'red'}]
        self.assertEqual(sorted_models(models), models)

    def test_multiple_models(self):
        models = [{'color': 'blue'}, {'color':'red'}, {'color': 'green'}]
        expected_result = [{'color': 'blue'}, {'color': 'green'}, {'color':'red'}]
        self.assertEqual(sorted_models(models), expected_result)

    def test_models_with_same_color(self):
        models = [{'color': 'blue'}, {'color': 'blue'}, {'color':'red'}]
        expected_result = [{'color': 'blue'}, {'color': 'blue'}, {'color':'red'}]
        self.assertEqual(sorted_models(models), expected_result)
