import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_typical_input(self):
        price = [['apple', '10.0'], ['banana', '5.0'], ['orange', '15.0']]
        self.assertEqual(float_sort(price), [['orange', '15.0'], ['apple', '10.0'], ['banana', '5.0']])

    def test_edge_case_reverse(self):
        price = [['apple', '10.0'], ['banana', '5.0'], ['orange', '15.0']]
        self.assertEqual(float_sort(price, reverse=False), [['banana', '5.0'], ['apple', '10.0'], ['orange', '15.0']])

    def test_edge_case_empty_input(self):
        price = []
        self.assertEqual(float_sort(price), [])

    def test_edge_case_single_input(self):
        price = [['apple', '10.0']]
        self.assertEqual(float_sort(price), [['apple', '10.0']])

    def test_edge_case_duplicates(self):
        price = [['apple', '10.0'], ['banana', '5.0'], ['orange', '15.0'], ['apple', '10.0']]
        self.assertEqual(float_sort(price), [['orange', '15.0'], ['apple', '10.0'], ['apple', '10.0'], ['banana', '5.0']])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            float_sort('invalid_input')

    def test_invalid_input_non_sublist(self):
        with self.assertRaises(TypeError):
            float_sort([1, 2, 3])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            float_sort([['apple', 10.0], ['banana', 5.0]])

    def test_invalid_input_non_float(self):
        with self.assertRaises(TypeError):
            float_sort([['apple', '10.0'], ['banana', 'five']])
