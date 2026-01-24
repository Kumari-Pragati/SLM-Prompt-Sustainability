import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 2, 1, 4, 5, 2, 3, 1]
        n = len(arr)
        k = 2
        self.assertEqual(first_Element(arr, n, k), 2)

    def test_edge_case_k_is_1(self):
        arr = [1, 2, 3, 2, 1, 4, 5, 2, 3, 1]
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_edge_case_k_is_n(self):
        arr = [1, 2, 3, 2, 1, 4, 5, 2, 3, 1]
        n = len(arr)
        k = n
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_edge_case_n_is_0(self):
        arr = []
        n = len(arr)
        k = 2
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_edge_case_k_is_0(self):
        arr = [1, 2, 3, 2, 1, 4, 5, 2, 3, 1]
        n = len(arr)
        k = 0
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_invalid_input_type(self):
        arr = [1, 2, 3, 2, 1, 4, 5, 2, 3, 1]
        n = len(arr)
        k = "two"
        with self.assertRaises(TypeError):
            first_Element(arr, n, k)
