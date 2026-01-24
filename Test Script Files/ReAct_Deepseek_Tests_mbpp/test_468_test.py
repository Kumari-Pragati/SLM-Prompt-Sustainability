import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 60)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 5)

    def test_edge_case_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), -1)

    def test_edge_case_all_positive_elements(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 120)

    def test_edge_case_all_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), -1)

    def test_edge_case_mixed_elements(self):
        arr = [-1, -2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 60)

    def test_error_case_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(ValueError):
            max_product(arr, n)

    def test_error_case_negative_length(self):
        arr = [1, 2, 3, 4, 5]
        n = -5
        with self.assertRaises(ValueError):
            max_product(arr, n)
