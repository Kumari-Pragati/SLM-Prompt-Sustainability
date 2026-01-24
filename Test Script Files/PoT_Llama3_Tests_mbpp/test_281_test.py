import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5]))

    def test_edge_case_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_edge_case_duplicates(self):
        self.assertFalse(all_unique([1, 1, 2, 3]))

    def test_edge_case_duplicates_at_end(self):
        self.assertFalse(all_unique([1, 2, 3, 1]))

    def test_edge_case_duplicates_at_start(self):
        self.assertFalse(all_unique([1, 1, 2, 3]))

    def test_edge_case_duplicates_at_start_and_end(self):
        self.assertFalse(all_unique([1, 1, 2, 1]))

    def test_edge_case_duplicates_at_start_and_middle(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 1]))

    def test_edge_case_duplicates_at_end_and_middle(self):
        self.assertFalse(all_unique([1, 2, 3, 1, 1]))

    def test_edge_case_duplicates_at_start_and_end_and_middle(self):
        self.assertFalse(all_unique([1, 1, 2, 1, 1]))
