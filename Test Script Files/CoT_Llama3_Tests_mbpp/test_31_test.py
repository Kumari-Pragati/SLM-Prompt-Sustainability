import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 2), [3, 4])

    def test_edge_case_k_zero(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 0), [])

    def test_edge_case_k_equal_to_length(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 3), [3, 4, 5])

    def test_invalid_input_non_integer_k(self):
        with self.assertRaises(TypeError):
            func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 'a')

    def test_invalid_input_non_list_input(self):
        with self.assertRaises(TypeError):
            func(123, 2)

    def test_empty_input(self):
        self.assertEqual(func([], 2), [])

    def test_single_element_input(self):
        self.assertEqual(func([[1]], 1), [1])
