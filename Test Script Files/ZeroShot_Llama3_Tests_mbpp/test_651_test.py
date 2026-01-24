import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_subset(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3, 4, 5), (1, 2, 3)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))
        self.assertFalse(check_subset((1, 2, 3, 4), (5, 6)))
        self.assertFalse(check_subset((1, 2, 3, 4, 5), (6, 7, 8)))

    def test_empty_subset(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((1, 2, 3), ()))

    def test_empty_superset(self):
        self.assertTrue(check_subset((1, 2, 3), ()))
        self.assertTrue(check_subset((1, 2, 3, 4), ()))
        self.assertTrue(check_subset((1, 2, 3, 4, 5), ()))

    def test_single_element_subset(self):
        self.assertTrue(check_subset((1, 2, 3), (1)))
        self.assertFalse(check_subset((1, 2, 3), (4)))

    def test_single_element_superset(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3, 4, 5), (1, 2, 3)))
