import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(modified_encode([1, 1, 1, 2, 2, 3]), [[3, 1], [2, 2], [1, 3]])

    def test_edge_condition_empty_input(self):
        self.assertEqual(modified_encode([]), [])

    def test_edge_condition_single_element(self):
        self.assertEqual(modified_encode([1]), [1])

    def test_boundary_condition_repeated_elements(self):
        self.assertEqual(modified_encode([1, 1, 1, 1]), [[4, 1]])

    def test_complex_case_mixed_elements(self):
        self.assertEqual(modified_encode([1, 2, 2, 3, 3, 3]), [[1, 1], [2, 2], [3, 3]])

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            modified_encode([1, 'a', 2])
