import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_no_duplicates(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4, 5]))

    def test_with_duplicates(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))
