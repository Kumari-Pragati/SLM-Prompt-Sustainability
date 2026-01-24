import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_subset(self):
        self.assertTrue(check_subset((1, 2, 3, 4, 5), (1, 2)))
        self.assertTrue(check_subset((1, 2, 3, 4, 5), (1, 2, 3, 4, 5)))
        self.assertFalse(check_subset((1, 2, 3, 4, 5), (6, 7)))
        self.assertFalse(check_subset((1, 2, 3, 4, 5), (1, 2, 3, 4, 5, 6)))

    def test_empty_tuples(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((1, 2, 3), ()))
        self.assertFalse(check_subset((), (1, 2, 3)))

    def test_single_element_tuples(self):
        self.assertTrue(check_subset((1,), (1,)))
        self.assertFalse(check_subset((1,), (2,)))
        self.assertFalse(check_subset((2,), (1,)))
