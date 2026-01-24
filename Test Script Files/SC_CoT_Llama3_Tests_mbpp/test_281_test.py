import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_all_unique_true(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5]))

    def test_all_unique_false(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4]))

    def test_all_unique_single_element(self):
        self.assertTrue(all_unique([1]))

    def test_all_unique_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_all_unique_single_repeated_element(self):
        self.assertFalse(all_unique([1, 1]))

    def test_all_unique_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_all_unique_list_with_duplicates(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4]))

    def test_all_unique_list_with_duplicates_and_unique(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4, 5]))

    def test_all_unique_list_with_duplicates_and_unique_and_duplicates(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4, 4, 5]))

    def test_all_unique_list_with_duplicates_and_unique_and_duplicates_and_unique(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4, 4, 5, 5]))
