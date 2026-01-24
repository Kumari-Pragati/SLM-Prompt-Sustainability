import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_edge_case_empty_lists(self):
        self.assertEqual(sub_list([], []), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(sub_list([1], [1]), [0])

    def test_special_case_negative_numbers(self):
        self.assertEqual(sub_list([-1, -2, -3], [-4, -5, -6]), [3, 3, 3])

    def test_invalid_input_different_lengths(self):
        with self.assertRaises(TypeError):
            sub_list([1, 2, 3], [1, 2])

    def test_invalid_input_non_list_arguments(self):
        with self.assertRaises(TypeError):
            sub_list("1, 2, 3", [1, 2, 3])
        with self.assertRaises(TypeError):
            sub_list([1, 2, 3], "1, 2, 3")
