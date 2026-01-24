import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_distinct((1, 2, 3, 4, 5)))

    def test_empty_tuple(self):
        self.assertTrue(check_distinct(()))

    def test_single_element(self):
        self.assertTrue(check_distinct((1,)))

    def test_duplicate_elements(self):
        self.assertFalse(check_distinct((1, 2, 2, 3, 4)))

    def test_large_tuple(self):
        self.assertTrue(check_distinct(tuple(range(1, 10001))))

    def test_large_duplicate_tuple(self):
        self.assertFalse(check_distinct(tuple(range(1, 10001)) + (1,)))

    def test_negative_numbers(self):
        self.assertTrue(check_distinct((-1, -2, -3, -4, -5)))

    def test_duplicate_negative_numbers(self):
        self.assertFalse(check_distinct((-1, -2, -2, -3, -4)))

    def test_mixed_numbers(self):
        self.assertTrue(check_distinct((-1, 0, 1, 2, 3, 4, 5)))

    def test_duplicate_mixed_numbers(self):
        self.assertFalse(check_distinct((-1, 0, 1, 2, 2, 3, 4)))
