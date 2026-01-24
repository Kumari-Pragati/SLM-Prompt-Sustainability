import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_duplicates(self):
        self.assertFalse(all_unique([1, 1, 2, 2, 3, 3]))

    def test_no_duplicates(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5]))

    def test_long_list(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_duplicates_at_end(self):
        self.assertFalse(all_unique([1, 2, 3, 4, 5, 5, 5]))

    def test_duplicates_in_middle(self):
        self.assertFalse(all_unique([1, 2, 3, 4, 5, 6, 6]))

    def test_duplicates_at_start(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 4, 5]))

    def test_duplicates_everywhere(self):
        self.assertFalse(all_unique([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
