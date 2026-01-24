import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_typical_input(self):
        price = [('apple', '10.0'), ('banana', '5.0'), ('orange', '15.0')]
        self.assertEqual(float_sort(price), [('orange', '15.0'), ('apple', '10.0'), ('banana', '5.0')])

    def test_edge_case_empty_list(self):
        price = []
        self.assertEqual(float_sort(price), [])

    def test_edge_case_single_element_list(self):
        price = [('apple', '10.0')]
        self.assertEqual(float_sort(price), [('apple', '10.0')])

    def test_edge_case_reverse_order(self):
        price = [('apple', '10.0'), ('banana', '5.0'), ('orange', '15.0')]
        self.assertEqual(float_sort(price, reverse=False), [('banana', '5.0'), ('apple', '10.0'), ('orange', '15.0')])

    def test_invalid_input_non_list(self):
        price = 'invalid input'
        with self.assertRaises(TypeError):
            float_sort(price)

    def test_invalid_input_non_string_in_list(self):
        price = [('apple', 10), ('banana', '5.0'), ('orange', '15.0')]
        with self.assertRaises(TypeError):
            float_sort(price)
