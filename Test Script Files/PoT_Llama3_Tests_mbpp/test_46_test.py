import unittest
from mbpp_46_code import test_distinct

class TestTestDistinct(unittest.TestCase):

    def test_typical(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_duplicates(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_empty(self):
        self.assertTrue(test_distinct([]))

    def test_single(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicates_at_start(self):
        self.assertFalse(test_distinct([1, 1, 2, 3, 4]))

    def test_duplicates_at_end(self):
        self.assertFalse(test_distinct([1, 2, 3, 4, 4]))

    def test_duplicates_in_middle(self):
        self.assertFalse(test_distinct([1, 2, 2, 3, 4]))

    def test_duplicates_everywhere(self):
        self.assertFalse(test_distinct([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
