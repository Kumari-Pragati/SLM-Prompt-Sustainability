import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element_array(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicates_array(self):
        self.assertTrue(test_duplicate([1, 1, 1]))

    def test_no_duplicates_array(self):
        self.assertFalse(test_duplicate([1, 2, 3]))

    def test_duplicates_and_non_duplicates_array(self):
        self.assertTrue(test_duplicate([1, 1, 2, 3]))

    def test_duplicates_and_duplicates_array(self):
        self.assertTrue(test_duplicate([1, 1, 1, 1]))

    def test_duplicates_and_duplicates_and_non_duplicates_array(self):
        self.assertTrue(test_duplicate([1, 1, 1, 2, 3]))
