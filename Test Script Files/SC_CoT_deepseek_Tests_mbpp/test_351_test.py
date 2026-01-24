import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):
    
    def test_typical_case(self):
        arr = [1, 7, 4, 3, 4, 8, 7]
        n = len(arr)
        k = 2
        self.assertEqual(first_Element(arr, n, k), 7)

    def test_edge_case_k_equals_one(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_edge_case_k_greater_than_max_frequency(self):
        arr = [1, 2, 2, 3, 3]
        n = len(arr)
        k = 4
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_invalid_input_negative_k(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = -1
        with self.assertRaises(Exception):
            first_Element(arr, n, k)

    def test_invalid_input_negative_elements(self):
        arr = [-1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), -1)
