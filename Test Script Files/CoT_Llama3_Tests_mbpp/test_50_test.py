import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_edge_case_empty_list(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_length_list([[1, 2, 3]]), (3, [1, 2, 3]))

    def test_edge_case_all_elements_of_same_length(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_edge_case_all_elements_of_different_lengths(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4], [5, 6, 7, 8, 9]]), (1, [4]))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            min_length_list("Invalid input")
