import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_typical_use_case(self):
        K = [1, 2, 3, 4, 5]
        test_tuple = (1, 2, 3)
        self.assertTrue(check_tuples(test_tuple, K))

    def test_edge_case_empty_K(self):
        K = []
        test_tuple = (1, 2, 3)
        self.assertFalse(check_tuples(test_tuple, K))

    def test_edge_case_empty_test_tuple(self):
        K = [1, 2, 3, 4, 5]
        test_tuple = ()
        self.assertFalse(check_tuples(test_tuple, K))

    def test_edge_case_single_element_K(self):
        K = [1]
        test_tuple = (1, 2, 3)
        self.assertFalse(check_tuples(test_tuple, K))

    def test_edge_case_single_element_test_tuple(self):
        K = [1, 2, 3, 4, 5]
        test_tuple = (1,)
        self.assertTrue(check_tuples(test_tuple, K))

    def test_edge_case_K_subset_of_test_tuple(self):
        K = [1, 2, 3]
        test_tuple = (1, 2, 3, 4, 5)
        self.assertTrue(check_tuples(test_tuple, K))

    def test_edge_case_K_superset_of_test_tuple(self):
        K = [1, 2, 3, 4, 5]
        test_tuple = (1, 2, 3)
        self.assertTrue(check_tuples(test_tuple, K))
