import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_typical_case(self):
        models = [{'color':'red', 'name':'model1'}, {'color': 'blue', 'name':'model2'}, {'color': 'green', 'name':'model3'}]
        self.assertEqual(sorted_models(models), [{'color': 'blue', 'name':'model2'}, {'color': 'green', 'name':'model3'}, {'color':'red', 'name':'model1'}])

    def test_edge_case_empty_list(self):
        models = []
        self.assertEqual(sorted_models(models), [])

    def test_edge_case_single_element_list(self):
        models = [{'color':'red', 'name':'model1'}]
        self.assertEqual(sorted_models(models), [{'color':'red', 'name':'model1'}])

    def test_edge_case_duplicates(self):
        models = [{'color':'red', 'name':'model1'}, {'color':'red', 'name':'model2'}, {'color': 'blue', 'name':'model3'}]
        self.assertEqual(sorted_models(models), [{'color': 'blue', 'name':'model3'}, {'color':'red', 'name':'model1'}, {'color':'red', 'name':'model2'}])

    def test_edge_case_invalid_input(self):
        models = 'not a list'
        with self.assertRaises(TypeError):
            sorted_models(models)
