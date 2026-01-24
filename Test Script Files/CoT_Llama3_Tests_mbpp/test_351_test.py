import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 2), 3)

    def test_edge_case_k_is_1(self):
        self.assertEqual(first_Element([1, 1, 2, 2, 3], 5, 1), 1)

    def test_edge_case_k_is_n(self):
        self.assertEqual(first_Element([1, 2, 3, 3, 4], 5, 5), 3)

    def test_edge_case_k_is_greater_than_n(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 10), -1)

    def test_edge_case_n_is_zero(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_edge_case_k_is_zero(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 0), -1)

    def test_invalid_input_non_integer_k(self):
        with self.assertRaises(TypeError):
            first_Element([1, 2, 3], 3, 'a')

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            first_Element([1, 2, 3], 'a', 2)
