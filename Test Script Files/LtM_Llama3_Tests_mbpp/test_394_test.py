import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_distinct((1, 2, 3)))
    def test_empty_input(self):
        self.assertFalse(check_distinct(()))
    def test_single_element(self):
        self.assertTrue(check_distinct((1,)))
    def test_duplicates(self):
        self.assertFalse(check_distinct((1, 1, 2)))
    def test_duplicates_at_start(self):
        self.assertFalse(check_distinct((1, 1, 2, 3)))
    def test_duplicates_at_end(self):
        self.assertFalse(check_distinct((1, 2, 3, 1)))
    def test_duplicates_in_middle(self):
        self.assertFalse(check_distinct((1, 2, 1, 3)))
    def test_duplicates_everywhere(self):
        self.assertFalse(check_distinct((1, 1, 2, 2, 3, 3)))
