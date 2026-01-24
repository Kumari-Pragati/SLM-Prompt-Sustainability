import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_tuples((1, 2, 3), []))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_tuples((1, 2, 3), [1]))

    def test_edge_case_all_elements_in_list(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_edge_case_no_elements_in_list(self):
        self.assertFalse(check_tuples((1, 2, 3), []))

    def test_edge_case_sublist(self):
        self.assertTrue(check_tuples((1, 2, 3, 4), [1, 2, 3]))

    def test_edge_case_superset(self):
        self.assertFalse(check_tuples((1, 2, 3, 4), [1, 2]))

    def test_edge_case_subset(self):
        self.assertTrue(check_tuples((1, 2, 3, 4), [1, 2, 3]))

    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_tuples((), [1, 2, 3]))

    def test_edge_case_single_element_tuple(self):
        self.assertTrue(check_tuples((1,), [1]))

    def test_edge_case_all_elements_in_tuple(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_edge_case_no_elements_in_tuple(self):
        self.assertFalse(check_tuples((1, 2, 3), []))

    def test_edge_case_subtuple(self):
        self.assertTrue(check_tuples((1, 2, 3, 4), [1, 2, 3]))

    def test_edge_case_supertuple(self):
        self.assertFalse(check_tuples((1, 2, 3, 4), [1, 2]))

    def test_edge_case_subtuplet(self):
        self.assertTrue(check_tuples((1, 2, 3, 4), [1, 2, 3]))
