import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))
        self.assertTrue(check_subset((1, 2, 3, 1), (1, 2)))
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 4)))

    def test_empty_inputs(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((), (1,)))
        self.assertTrue(check_subset((1, 2), ()))
        self.assertFalse(check_subset((1, 2), (1,)))

    def test_single_element_inputs(self):
        self.assertTrue(check_subset((1,), (1)))
        self.assertFalse(check_subset((1,), (2)))
        self.assertTrue(check_subset((1, 2), (1)))
        self.assertFalse(check_subset((1, 2), (2)))

    def test_duplicates_in_inputs(self):
        self.assertTrue(check_subset((1, 2, 2), (1, 2)))
        self.assertFalse(check_subset((1, 2, 2), (3, 4)))
        self.assertTrue(check_subset((1, 2, 2, 1), (1, 2)))
        self.assertFalse(check_subset((1, 2, 2), (1, 2, 3)))
