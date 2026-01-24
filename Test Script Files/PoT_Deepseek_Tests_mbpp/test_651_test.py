import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))

    def test_empty_subset(self):
        self.assertTrue(check_subset((1, 2, 3), ()))

    def test_empty_main_set(self):
        self.assertFalse(check_subset((), (1, 2)))

    def test_full_set(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (1, 2)))

    def test_duplicate_elements_in_subset(self):
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 2)))

    def test_subset_larger_than_main_set(self):
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 3, 4)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_subset("not a tuple", (1, 2))
