import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 3))

    def test_empty_list(self):
        self.assertFalse(check_element([], 3))

    def test_element_not_in_list(self):
        self.assertFalse(check_element([1, 2, 3, 4, 5], 6))

    def test_list_with_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 3, 3], 3))

    def test_list_with_duplicates_and_non_match(self):
        self.assertFalse(check_element([1, 2, 2, 3, 3, 3], 4))

    def test_list_with_duplicates_and_non_match_edge(self):
        self.assertFalse(check_element([1, 2, 2, 3, 3, 3], 1))

    def test_list_with_duplicates_and_non_match_edge2(self):
        self.assertFalse(check_element([1, 2, 2, 3, 3, 3], 2))

    def test_list_with_duplicates_and_non_match_edge3(self):
        self.assertFalse(check_element([1, 2, 2, 3, 3, 3], 3))
