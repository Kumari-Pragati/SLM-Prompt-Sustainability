import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 5)

    def test_edge_case_single_pair(self):
        self.assertEqual(max_difference([(1, 2)]), 1)

    def test_edge_case_same_elements(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            max_difference("not a list")

    def test_invalid_input_elements(self):
        with self.assertRaises(TypeError):
            max_difference([(1, "not a number"), (2, 2), (3, 3)])
