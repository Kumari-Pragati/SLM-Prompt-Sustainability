import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_typical_case(self):
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
        self.assertEqual(float_sort(price, reverse=False), [('apple', '10.0'), ('banana', '5.0'), ('orange', '15.0')])

    def test_edge_case_non_numeric_price(self):
        price = [('apple', 'ten'), ('banana', 'five'), ('orange', 'fifteen')]
        with self.assertRaises(ValueError):
            float_sort(price)

    def test_edge_case_non_list_input(self):
        price = 'apple'
        with self.assertRaises(TypeError):
            float_sort(price)
