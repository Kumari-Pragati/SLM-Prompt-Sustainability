import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(check_distinct((1, 2, 3)))

    def test_edge_case_empty(self):
        self.assertTrue(check_distinct(()))

    def test_edge_case_single_element(self):
        self.assertTrue(check_distinct((1,)))

    def test_edge_case_duplicates(self):
        self.assertFalse(check_distinct((1, 2, 2)))

    def test_edge_case_duplicates_at_start(self):
        self.assertFalse(check_distinct((2, 2, 3)))

    def test_edge_case_duplicates_at_end(self):
        self.assertFalse(check_distinct((1, 2, 2)))

    def test_edge_case_duplicates_at_start_and_end(self):
        self.assertFalse(check_distinct((2, 2, 2)))

    def test_edge_case_duplicates_at_start_and_middle(self):
        self.assertFalse(check_distinct((2, 2, 3)))

    def test_edge_case_duplicates_at_middle_and_end(self):
        self.assertFalse(check_distinct((1, 2, 2)))

    def test_edge_case_duplicates_at_start_and_middle_and_end(self):
        self.assertFalse(check_distinct((2, 2, 2)))

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            check_distinct("abc")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            check_distinct(123)
