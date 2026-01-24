import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_edge_case_empty_k(self):
        self.assertFalse(check_tuples((1, 2, 3), []))

    def test_edge_case_empty_test_tuple(self):
        self.assertFalse(check_tuples(tuple(), [1, 2, 3]))

    def test_edge_case_k_subset_of_test_tuple(self):
        self.assertFalse(check_tuples((1, 2, 3), [1, 2]))

    def test_edge_case_k_superset_of_test_tuple(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3, 4]))

    def test_edge_case_k_equal_to_test_tuple(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_edge_case_k_subset_of_test_tuple_with_duplicates(self):
        self.assertFalse(check_tuples((1, 2, 2, 3), [1, 2]))

    def test_edge_case_k_superset_of_test_tuple_with_duplicates(self):
        self.assertTrue(check_tuples((1, 2, 2, 3), [1, 2, 3, 4]))

    def test_edge_case_k_equal_to_test_tuple_with_duplicates(self):
        self.assertTrue(check_tuples((1, 2, 2, 3), [1, 2, 2, 3]))
