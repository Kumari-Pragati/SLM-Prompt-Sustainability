import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicate_elements(self):
        self.assertTrue(test_duplicate([1, 1]))
        self.assertTrue(test_duplicate([1, 2, 1]))
        self.assertTrue(test_duplicate([1, 2, 3, 1]))

    def test_unique_elements(self):
        self.assertFalse(test_duplicate([1, 2, 3]))
        self.assertFalse(test_duplicate([10, 20, 30]))
        self.assertFalse(test_duplicate([-1, 0, 1]))
