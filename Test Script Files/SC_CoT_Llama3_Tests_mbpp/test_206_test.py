import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (2, 4, 6))

    def test_edge_case_empty(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(concatenate_elements((1,)), ())

    def test_edge_case_two_elements(self):
        self.assertEqual(concatenate_elements((1, 2)), (3,))

    def test_edge_case_three_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (2, 4, 6))

    def test_edge_case_four_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), (3, 6, 9))

    def test_edge_case_five_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), (3, 6, 9, 12))

    def test_edge_case_long_input(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), (3, 6, 9, 12, 15))

    def test_edge_case_long_input_with_zero(self):
        self.assertEqual(concatenate_elements((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)), (1, 3, 6, 9, 12))

    def test_edge_case_long_input_with_zero_at_end(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)), (3, 6, 9, 12, 15))

    def test_edge_case_long_input_with_zero_at_start(self):
        self.assertEqual(concatenate_elements((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)), (1, 3, 6, 9, 12))

    def test_edge_case_long_input_with_zero_at_start_and_end(self):
        self.assertEqual(concatenate_elements((0, 1, 2, 3, 4, 5, 6, 7, 8, 0)), (1, 3, 6, 9, 12))
