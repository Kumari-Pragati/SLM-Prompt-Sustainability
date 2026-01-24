import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_edge_case_empty_string(self):
        self.assertFalse(find_substring(["hello", "world", "python"], ""))

    def test_edge_case_empty_list(self):
        self.assertFalse(find_substring([], "world"))

    def test_edge_case_single_element_list(self):
        self.assertTrue(find_substring(["world"], "world"))

    def test_edge_case_substring_not_found(self):
        self.assertFalse(find_substring(["hello", "python"], "java"))

    def test_edge_case_substring_found_in_multiple_strings(self):
        self.assertTrue(find_substring(["hello", "world", "python", "java"], "world"))

    def test_edge_case_substring_found_in_first_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "hello"))

    def test_edge_case_substring_found_in_last_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "python"))

    def test_edge_case_substring_found_in_middle_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_edge_case_substring_not_found_in_list(self):
        self.assertFalse(find_substring(["hello", "python"], "java"))

    def test_edge_case_substring_found_in_list(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_edge_case_substring_found_in_first_and_last_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "hello"))

    def test_edge_case_substring_found_in_first_and_middle_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "hello"))

    def test_edge_case_substring_found_in_last_and_middle_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_edge_case_substring_found_in_first_and_last_and_middle_string(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))
