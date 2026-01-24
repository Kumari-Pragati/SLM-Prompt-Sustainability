import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2]))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_element((1, 2, 3), []))

    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_element((), [1, 2]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_element((1, 2, 3), [1]))

    def test_edge_case_single_element_tuple(self):
        self.assertTrue(check_element((1,), [1]))

    def test_edge_case_list_subset(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2]))

    def test_edge_case_tuple_subset(self):
        self.assertTrue(check_element((1, 2, 3), (1, 2)))

    def test_edge_case_list_superset(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))

    def test_edge_case_tuple_superset(self):
        self.assertTrue(check_element((1, 2, 3), (1, 2, 3)))

    def test_edge_case_list_subset_with_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3), [1, 2]))

    def test_edge_case_tuple_subset_with_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3), (1, 2)))

    def test_edge_case_list_superset_with_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3), [1, 2, 3]))

    def test_edge_case_tuple_superset_with_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3), (1, 2, 3)))

    def test_edge_case_list_subset_with_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3), [1, 2]))

    def test_edge_case_tuple_subset_with_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3), (1, 2)))

    def test_edge_case_list_superset_with_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3), [1, 2, 3]))

    def test_edge_case_tuple_superset_with_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3), (1, 2, 3)))

    def test_edge_case_list_subset_with_duplicates_and_empty_and_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2), [1, 2]))

    def test_edge_case_tuple_subset_with_duplicates_and_empty_and_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2), (1, 2)))

    def test_edge_case_list_superset_with_duplicates_and_empty_and_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2), [1, 2, 3]))

    def test_edge_case_tuple_superset_with_duplicates_and_empty_and_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2), (1, 2, 3)))

    def test_edge_case_list_subset_with_duplicates_and_empty_and_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2, 2), [1, 2]))

    def test_edge_case_tuple_subset_with_duplicates_and_empty_and_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2, 2), (1, 2)))

    def test_edge_case_list_superset_with_duplicates_and_empty_and_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2, 2), [1, 2, 3]))

    def test_edge_case_tuple_superset_with_duplicates_and_empty_and_duplicates_and_empty(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2, 2), (1, 2, 3)))

    def test_edge_case_list_subset_with_duplicates_and_empty_and_duplicates_and_empty_and_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2, 2, 2), [1, 2]))

    def test_edge_case_tuple_subset_with_duplicates_and_empty_and_duplicates_and_empty_and_duplicates(self):
        self.assertTrue(check_element((1, 2, 2, 3, 2, 2, 2), (1,