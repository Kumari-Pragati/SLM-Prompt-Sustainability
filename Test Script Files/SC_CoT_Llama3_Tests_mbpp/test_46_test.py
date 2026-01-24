import unittest
from mbpp_46_code import test_distinct

class TestTestDistinct(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element_list(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicates_list(self):
        self.assertFalse(test_distinct([1, 1, 2]))

    def test_duplicates_list_with_duplicates(self):
        self.assertFalse(test_distinct([1, 1, 1, 2]))

    def test_no_duplicates_list(self):
        self.assertTrue(test_distinct([1, 2, 3]))

    def test_no_duplicates_list_with_duplicates(self):
        self.assertTrue(test_distinct([1, 2, 3, 4]))

    def test_empty_set(self):
        self.assertTrue(test_distinct([]))

    def test_single_element_set(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicates_set(self):
        self.assertFalse(test_distinct([1, 1, 2]))

    def test_duplicates_set_with_duplicates(self):
        self.assertFalse(test_distinct([1, 1, 1, 2]))

    def test_no_duplicates_set(self):
        self.assertTrue(test_distinct([1, 2, 3]))

    def test_no_duplicates_set_with_duplicates(self):
        self.assertTrue(test_distinct([1, 2, 3, 4]))
