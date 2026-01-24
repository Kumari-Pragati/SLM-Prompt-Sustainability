import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_distinct(self):
        self.assertTrue(check_distinct((1, 2, 3)))
    def test_non_distinct(self):
        self.assertFalse(check_distinct((1, 2, 2)))
    def test_empty(self):
        self.assertTrue(check_distinct(()))
    def test_single_element(self):
        self.assertTrue(check_distinct((1,)))
    def test_duplicates(self):
        self.assertFalse(check_distinct((1, 1, 2, 2)))
    def test_large_input(self):
        self.assertFalse(check_distinct((1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6)))
