import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        result = max_product(arr)
        self.assertEqual(result, (3, 4))

    def test_edge_case_single_element(self):
        arr = [1]
        result = max_product(arr)
        self.assertEqual(result, None)

    def test_edge_case_two_elements(self):
        arr = [1, 2]
        result = max_product(arr)
        self.assertEqual(result, (1, 2))

    def test_edge_case_three_elements(self):
        arr = [1, 2, 3]
        result = max_product(arr)
        self.assertEqual(result, (2, 3))

    def test_edge_case_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        result = max_product(arr)
        self.assertEqual(result, (-1, -2))

    def test_edge_case_zero(self):
        arr = [0, 1, 2, 3, 4]
        result = max_product(arr)
        self.assertEqual(result, (0, 1))

    def test_invalid_input_empty_array(self):
        arr = []
        result = max_product(arr)
        self.assertEqual(result, None)

    def test_invalid_input_non_array_input(self):
        arr = "hello"
        with self.assertRaises(TypeError):
            max_product(arr)
