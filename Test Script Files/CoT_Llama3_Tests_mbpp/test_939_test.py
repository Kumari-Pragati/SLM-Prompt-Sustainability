import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_sorted_models(self):
        models = [{'color':'red', 'name':'model1'}, {'color': 'blue', 'name':'model2'}, {'color': 'green', 'name':'model3'}]
        expected_output = [{'color': 'blue', 'name':'model2'}, {'color': 'green', 'name':'model3'}, {'color':'red', 'name':'model1'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_sorted_models_empty_list(self):
        models = []
        expected_output = []
        self.assertEqual(sorted_models(models), expected_output)

    def test_sorted_models_single_element(self):
        models = [{'color':'red', 'name':'model1'}]
        expected_output = [{'color':'red', 'name':'model1'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_sorted_models_multiple_colors(self):
        models = [{'color':'red', 'name':'model1'}, {'color': 'blue', 'name':'model2'}, {'color':'red', 'name':'model3'}, {'color': 'blue', 'name':'model4'}]
        expected_output = [{'color': 'blue', 'name':'model2'}, {'color': 'blue', 'name':'model4'}, {'color':'red', 'name':'model1'}, {'color':'red', 'name':'model3'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_sorted_models_invalid_input(self):
        models = 'not a list'
        with self.assertRaises(TypeError):
            sorted_models(models)
