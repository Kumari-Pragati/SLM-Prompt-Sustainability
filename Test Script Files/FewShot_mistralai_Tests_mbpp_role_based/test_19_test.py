import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):
    def test_duplicate_present(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))

    def test_duplicate_absent(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))
