import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))

    def test_edge_case_empty_sets(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((1,), ()))

    def test_edge_case_single_element(self):
        self.assertTrue(check_subset((1,), (1,)))
        self.assertFalse(check_subset((1,), (2,)))

    def test_edge_case_duplicate_elements(self):
        self.assertTrue(check_subset((1, 1, 2), (1, 2)))
        self.assertTrue(check_subset((1, 2, 2), (1, 2)))

    def test_edge_case_reversed_sets(self):
        self.assertTrue(check_subset((1, 2), (2, 1)))
        self.assertFalse(check_subset((1, 2, 3), (3, 2, 1)))

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, check_subset, (1, 2, 3), 'abc')
        self.assertRaises(TypeError, check_subset, 'abc', (1, 2, 3))
