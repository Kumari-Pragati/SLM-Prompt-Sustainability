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

    def test_duplicates_at_end(self):
        self.assertFalse(all_unique([1, 2, 3, 1]))

    def test_duplicates_at_start(self):
        self.assertFalse(all_unique([1, 1, 2, 3]))

    def test_duplicates_in_middle(self):
        self.assertFalse(all_unique([1, 2, 1, 3, 4]))

    def test_duplicates_at_start_and_end(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 1]))

    def test_duplicates_at_start_and_middle(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 1, 2]))

    def test_duplicates_at_end_and_middle(self):
        self.assertFalse(all_unique([1, 2, 1, 3, 4, 2]))

    def test_duplicates_at_start_and_end_and_middle(self):
        self.assertFalse(all_unique([1, 1, 2, 3, 1, 2, 1]))
