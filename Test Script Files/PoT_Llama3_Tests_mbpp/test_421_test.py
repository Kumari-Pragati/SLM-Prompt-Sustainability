import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_edge_case_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_edge_case_single_element_tuple_with_delimiter(self):
        self.assertEqual(concatenate_tuple((1,)), '1-')

    def test_edge_case_tuple_with_single_element_and_delimiter(self):
        self.assertEqual(concatenate_tuple((1,)), '1-')

    def test_edge_case_tuple_with_multiple_elements_and_delimiter(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_edge_case_tuple_with_multiple_elements_and_delimiter_at_end(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_edge_case_tuple_with_multiple_elements_and_delimiter_at_start(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_edge_case_tuple_with_multiple_elements_and_delimiter_at_start_and_end(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_edge_case_tuple_with_multiple_elements_and_delimiter_at_start_and_end_and_middle(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')
