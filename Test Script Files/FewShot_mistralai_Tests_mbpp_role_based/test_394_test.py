import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_distinct_positive_numbers(self):
        self.assertTrue(check_distinct((1, 2, 3, 4)))
        self.assertTrue(check_distinct((5, 6, 7, 8)))

    def test_distinct_empty_list(self):
        self.assertTrue(check_distinct([]))

    def test_distinct_single_element(self):
        self.assertTrue(check_distinct((1,)))

    def test_distinct_duplicate_elements(self):
        self.assertFalse(check_distinct((1, 1, 2, 3)))

    def test_distinct_negative_numbers(self):
        self.assertTrue(check_distinct((-1, -2, -3, -4)))

    def test_distinct_mixed_numbers(self):
        self.assertTrue(check_distinct((1, -2, 3, -4)))
