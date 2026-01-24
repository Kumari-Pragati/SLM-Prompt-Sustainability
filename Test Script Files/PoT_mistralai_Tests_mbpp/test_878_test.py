import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))

    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_tuples((), {1, 2, 3}))

    def test_edge_case_empty_set(self):
        self.assertTrue(check_tuples((1, 2, 3), {}))

    def test_edge_case_single_element(self):
        self.assertTrue(check_tuples((1,), {1}))
        self.assertFalse(check_tuples((2,), {1}))

    def test_edge_case_single_element_set(self):
        self.assertTrue(check_tuples((1,), {1}))
        self.assertFalse(check_tuples((2,), {1}))

    def test_edge_case_different_lengths(self):
        self.assertFalse(check_tuples((1, 2, 3), {1, 2}))

    def test_corner_case_none_in_set(self):
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6}))
