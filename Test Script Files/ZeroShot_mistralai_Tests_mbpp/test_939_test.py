import unittest
from mbpp_939_code import sorted_models

class TestSortedModels(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sorted_models([]), [])

    def test_single_model(self):
        model = {'color': 'red'}
        self.assertEqual(sorted_models([model]), [model])

    def test_multiple_models_same_color(self):
        model1 = {'color': 'red'}
        model2 = {'color': 'red'}
        self.assertEqual(sorted_models([model1, model2]), [model1, model2])

    def test_multiple_models_different_colors(self):
        model1 = {'color': 'red'}
        model2 = {'color': 'blue'}
        self.assertEqual(sorted_models([model1, model2]), [model1, model2])

    def test_models_with_case_insensitive_color(self):
        model1 = {'color': 'Red'}
        model2 = {'color': 'blue'}
        self.assertEqual(sorted_models([model1, model2]), [model1, model2])

    def test_models_with_different_color_order(self):
        model1 = {'color': ['red', 'green']}
        model2 = {'color': ['green', 'red']}
        self.assertEqual(sorted_models([model1, model2]), [model1, model2])
