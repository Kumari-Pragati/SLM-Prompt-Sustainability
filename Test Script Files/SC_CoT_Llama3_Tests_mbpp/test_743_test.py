import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_edge_case_m_zero(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 1), [1, 2, 3, 4, 5])

    def test_edge_case_n_zero(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 0), [3, 4, 5, 1, 2])

    def test_edge_case_m_equal_to_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 1), [5, 1, 2, 3, 4])

    def test_edge_case_n_equal_to_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 1, 5), [4, 5, 1, 2, 3])

    def test_edge_case_m_greater_than_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 10, 1), [4, 5, 1, 2, 3])

    def test_edge_case_n_greater_than_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 1, 10), [4, 5, 1, 2, 3])

    def test_invalid_input_type_m(self):
        with self.assertRaises(TypeError):
            rotate_right([1, 2, 3, 4, 5], 'a', 1)

    def test_invalid_input_type_n(self):
        with self.assertRaises(TypeError):
            rotate_right([1, 2, 3, 4, 5], 1, 'a')
