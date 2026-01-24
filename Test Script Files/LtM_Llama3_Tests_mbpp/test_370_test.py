import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(float_sort([[1, 'a'], [2, 'b'], [3, 'c']]), [[3, 'c'], [2, 'b'], [1, 'a']])

    def test_empty_input(self):
        self.assertEqual(float_sort([]), [])

    def test_single_element_input(self):
        self.assertEqual(float_sort([[1, 'a']]), [[1, 'a']])

    def test_reverse_order(self):
        self.assertEqual(float_sort([[1, 'a'], [2, 'b'], [3, 'c']], reverse=False), [[1, 'a'], [2, 'b'], [3, 'c']])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            float_sort([1, 2, 3])

    def test_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            float_sort([[1], [2, 'b'], [3, 'c', 'd']])
