import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sorted_models([]), [])

    def test_single_model(self):
        self.assertEqual(sorted_models([{'color':'red', 'name':'model1'}]), [{'color':'red', 'name':'model1'}])

    def test_multiple_models(self):
        self.assertEqual(sorted_models([{'color':'red', 'name':'model1'}, {'color': 'blue', 'name':'model2'}, {'color':'red', 'name':'model3'}]), 
                         [{'color': 'blue', 'name':'model2'}, {'color':'red', 'name':'model1'}, {'color':'red', 'name':'model3'}])

    def test_models_with_same_color(self):
        self.assertEqual(sorted_models([{'color':'red', 'name':'model1'}, {'color':'red', 'name':'model2'}, {'color': 'blue', 'name':'model3'}]), 
                         [{'color': 'blue', 'name':'model3'}, {'color':'red', 'name':'model1'}, {'color':'red', 'name':'model2'}])

    def test_models_with_same_color_and_name(self):
        self.assertEqual(sorted_models([{'color':'red', 'name':'model1'}, {'color':'red', 'name':'model1'}, {'color': 'blue', 'name':'model3'}]), 
                         [{'color': 'blue', 'name':'model3'}, {'color':'red', 'name':'model1'}, {'color':'red', 'name':'model1'}])
