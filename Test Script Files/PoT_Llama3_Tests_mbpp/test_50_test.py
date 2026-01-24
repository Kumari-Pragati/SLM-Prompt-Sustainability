import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_edge_case_empty_list(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_length_list([[1, 2, 3]]), (3, [1, 2, 3]))

    def test_edge_case_all_equal_length(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_edge_case_min_length_zero(self):
        self.assertEqual(min_length_list([[], [1, 2, 3], [4, 5, 6]]), (0, []))

    def test_edge_case_min_length_one(self):
        self.assertEqual(min_length_list([[], [1], [4, 5, 6]]), (1, [1]))

    def test_edge_case_min_length_multiple(self):
        self.assertEqual(min_length_list([[], [1], [4, 5, 6], [7, 8, 9]]), (1, [1]))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            min_length_list("Invalid input")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            min_length_list(123)
