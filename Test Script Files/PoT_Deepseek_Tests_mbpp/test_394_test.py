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

    def test_duplicate_in_middle(self):
        self.assertFalse(check_distinct((1, 2, 2, 4)))

    def test_duplicate_at_start(self):
        self.assertFalse(check_distinct((1, 1, 3, 4)))

    def test_duplicate_at_end(self):
        self.assertFalse(check_distinct((1, 2, 3, 4, 4)))

    def test_large_tuple(self):
        self.assertTrue(check_distinct(tuple(range(1, 1001))))

    def test_large_duplicate_tuple(self):
        self.assertFalse(check_distinct(tuple(range(1, 1001)) + (1,)))
