import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertTrue(check_distinct(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_distinct((1,)))

    def test_distinct_elements(self):
        self.assertTrue(check_distinct((1, 2, 3)))

    def test_repeated_elements(self):
        self.assertFalse(check_distinct((1, 1, 2)))

    def test_repeated_elements_with_duplicates(self):
        self.assertFalse(check_distinct((1, 1, 1, 2)))

    def test_empty_set(self):
        self.assertTrue(check_distinct(()))

    def test_single_element_set(self):
        self.assertTrue(check_distinct((1,)))

    def test_distinct_elements_set(self):
        self.assertTrue(check_distinct((1, 2, 3)))

    def test_repeated_elements_set(self):
        self.assertFalse(check_distinct((1, 1, 2)))

    def test_repeated_elements_with_duplicates_set(self):
        self.assertFalse(check_distinct((1, 1, 1, 2)))
