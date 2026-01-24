import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), (3, 6, 9))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(concatenate_elements((1,)), (1, 1))

    def test_edge_case_single_element_in_longer_tuple(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 1)), (3, 6, 9, 1))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(concatenate_elements((-1, 2, -3, 4)), (1, -1, -2, 1))
