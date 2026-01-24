import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 2
        self.assertEqual(first_Element(arr, n, k), 2)

    def test_edge_case_k_is_1(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 1
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_edge_case_k_is_n(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 5
        self.assertEqual(first_Element(arr, n, k), 5)

    def test_edge_case_n_is_0(self):
        arr = []
        n = 0
        k = 1
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_edge_case_k_is_greater_than_n(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 10
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_error_case_non_integer_input(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 'a'
        with self.assertRaises(TypeError):
            first_Element(arr, n, k)

    def test_error_case_non_integer_input_in_arr(self):
        arr = [1, 2, 3, 'a', 5]
        n = 5
        k = 2
        with self.assertRaises(TypeError):
            first_Element(arr, n, k)
