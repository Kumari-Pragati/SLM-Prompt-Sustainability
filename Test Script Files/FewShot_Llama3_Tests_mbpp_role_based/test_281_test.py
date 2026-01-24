import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_duplicates(self):
        self.assertFalse(all_unique([1, 1, 2, 2]))

    def test_no_duplicates(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))

    def test_large_list(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 4, 5]))
