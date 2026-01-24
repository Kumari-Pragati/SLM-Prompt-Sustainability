import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_subset(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertFalse(check_subset((1, 2, 3), (1, 4)))
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6)))
        self.assertFalse(check_subset((1, 2, 3), ()))
        self.assertTrue(check_subset((1, 2, 3), (1,)))
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 3, 4)))
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 3, 4, 5)))
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 3, 4, 5, 6)))

    def test_non_subset(self):
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6, 7)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6, 7, 8)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6, 7, 8, 9)))

    def test_empty(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((1, 2, 3), ()))

    def test_single(self):
        self.assertTrue(check_subset((1, 2, 3), (1)))
        self.assertFalse(check_subset((1, 2, 3), (4)))
