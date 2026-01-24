import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 5]))

    def test_duplicate_present(self):
        self.assertFalse(test_duplicate([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicate_at_boundary(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4, 4]))

    def test_duplicate_at_corner(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4, 5, 5]))

    def test_duplicate_at_start(self):
        self.assertFalse(test_duplicate([1, 1, 2, 3, 4]))

    def test_duplicate_at_end(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4, 4]))
