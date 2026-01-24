import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = 3
        self.assertEqual(find_Product(arr, n), 2)

    def test_edge_case_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(find_Product(arr, n), 1)

    def test_edge_case_single_element_array(self):
        arr = [1]
        n = 1
        self.assertEqual(find_Product(arr, n), 1)

    def test_edge_case_zero_elements(self):
        arr = [1, 2, 3]
        n = 0
        self.assertEqual(find_Product(arr, n), 1)

    def test_edge_case_negative_elements(self):
        arr = [-1, -2, -3]
        n = 2
        self.assertEqual(find_Product(arr, n), -2)

    def test_edge_case_non_integer_elements(self):
        arr = [1.5, 2.5, 3.5]
        n = 2
        self.assertEqual(find_Product(arr, n), 2.5)

    def test_edge_case_invalid_input_type(self):
        arr = [1, 2, 3]
        n = 'a'
        with self.assertRaises(TypeError):
            find_Product(arr, n)
