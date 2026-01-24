import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(even_position([0, 2, 4, 6]))

    def test_edge_case_single_element(self):
        self.assertTrue(even_position([0]))

    def test_boundary_case_empty_list(self):
        self.assertTrue(even_position([]))

    def test_corner_case_odd_length_list(self):
        self.assertFalse(even_position([0, 1, 2]))

    def test_typical_case_with_negative_numbers(self):
        self.assertTrue(even_position([-2, 0, 2, 4]))

    def test_edge_case_negative_single_element(self):
        self.assertTrue(even_position([-2]))

    def test_corner_case_odd_length_list_with_negative_numbers(self):
        self.assertFalse(even_position([-1, 0, 1]))

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            even_position([0, '2', 4])

    def test_invalid_input_mixed_types(self):
        with self.assertRaises(TypeError):
            even_position([0, '2', 4, 6])
