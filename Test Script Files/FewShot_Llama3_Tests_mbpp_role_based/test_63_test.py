import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 3), (2, 4), (5, 7)]
        self.assertEqual(max_difference(test_list), 2)

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(max_difference(test_list), 0)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 1)]
        self.assertEqual(max_difference(test_list), 0)

    def test_edge_case_two_element_list(self):
        test_list = [(1, 2)]
        self.assertEqual(max_difference(test_list), 1)

    def test_edge_case_three_element_list(self):
        test_list = [(1, 2), (2, 3), (3, 4)]
        self.assertEqual(max_difference(test_list), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_difference("not a list")
