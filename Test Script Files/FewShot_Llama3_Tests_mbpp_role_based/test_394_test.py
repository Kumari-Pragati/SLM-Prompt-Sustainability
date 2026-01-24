import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_distinct_elements(self):
        self.assertTrue(check_distinct((1, 2, 3, 4, 5)))

    def test_repeated_elements(self):
        self.assertFalse(check_distinct((1, 2, 2, 3, 4)))

    def test_empty_tuple(self):
        self.assertTrue(check_distinct(()))

    def test_single_element(self):
        self.assertTrue(check_distinct((1,)))

    def test_all_duplicates(self):
        self.assertFalse(check_distinct((1, 1, 1, 1)))

    def test_mixed_elements(self):
        self.assertTrue(check_distinct((1, 2, 3, 4, 5, 6)))
