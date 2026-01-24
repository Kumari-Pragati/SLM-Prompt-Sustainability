import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):
    def test_typical_input(self):
        models = [{'color':'red', 'name':'model1'}, 
                  {'color': 'blue', 'name':'model2'}, 
                  {'color': 'green', 'name':'model3'}]
        expected_output = [{'color': 'blue', 'name':'model2'}, 
                           {'color': 'green', 'name':'model3'}, 
                           {'color':'red', 'name':'model1'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_edge_case(self):
        models = [{'color':'red', 'name':'model1'}, 
                  {'color': 'blue', 'name':'model2'}]
        expected_output = [{'color': 'blue', 'name':'model2'}, 
                           {'color':'red', 'name':'model1'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_empty_input(self):
        models = []
        expected_output = []
        self.assertEqual(sorted_models(models), expected_output)

    def test_single_input(self):
        models = [{'color':'red', 'name':'model1'}]
        expected_output = [{'color':'red', 'name':'model1'}]
        self.assertEqual(sorted_models(models), expected_output)

    def test_invalid_input(self):
        models = 'not a list'
        with self.assertRaises(TypeError):
            sorted_models(models)
