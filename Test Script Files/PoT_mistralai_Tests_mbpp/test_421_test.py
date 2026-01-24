import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_edge_case_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_edge_case_two_elements_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2)), '1-2')

    def test_boundary_case_first_element_is_zero(self):
        self.assertEqual(concatenate_tuple((0, 1, 2)), '0-1-2')

    def test_boundary_case_last_element_is_zero(self):
        self.assertEqual(concatenate_tuple((1, 2, 0)), '1-2-0')

    def test_boundary_case_first_and_last_element_is_zero(self):
        self.assertEqual(concatenate_tuple((0, 1, 0)), '0-1-0')
