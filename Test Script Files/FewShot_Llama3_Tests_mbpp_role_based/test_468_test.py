import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 20)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_product(arr, n), 0)

    def test_edge_case_single_element_array(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 5)

    def test_edge_case_all_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), -5)

    def test_edge_case_all_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 20)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 20)

    def test_invalid_input_non_integer_array(self):
        arr = ['a', 'b', 'c', 'd', 'e']
        n = len(arr)
        with self.assertRaises(TypeError):
            max_product(arr, n)
