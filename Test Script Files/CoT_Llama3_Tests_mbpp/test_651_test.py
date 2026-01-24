import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_subset_true(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))

    def test_subset_false(self):
        self.assertFalse(check_subset((1, 2, 3, 4), (5, 6)))

    def test_subset_empty(self):
        self.assertTrue(check_subset((1, 2, 3, 4), ()))

    def test_subset_single_element(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1)))

    def test_subset_subset_of_subset(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2)))

    def test_subset_subset_of_subset2(self):
        self.assertTrue(check_subset((1, 2, 3, 4, 5), (1, 2, 3)))

    def test_subset_subset_of_subset3(self):
        self.assertFalse(check_subset((1, 2, 3, 4), (1, 2, 3, 5)))

    def test_subset_subset_of_subset4(self):
        self.assertFalse(check_subset((1, 2, 3, 4, 5), (1, 2, 3, 4, 5)))

    def test_subset_subset_of_subset5(self):
        self.assertTrue(check_subset((1, 2, 3, 4, 5), (1, 2, 3, 4)))

    def test_subset_subset_of_subset6(self):
        self.assertFalse(check_subset((1, 2, 3, 4, 5), (1, 2, 3, 4, 5, 6)))

    def test_subset_subset_of_subset7(self):
        self.assertFalse(check_subset((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6)))

    def test_subset_subset_of_subset8(self):
        self.assertTrue(check_subset((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5)))

    def test_subset_subset_of_subset9(self):
        self.assertFalse(check_subset((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6, 7)))

    def test_subset_subset_of_subset10(self):
        self.assertFalse(check_subset((1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7)))
