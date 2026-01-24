import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))

    def test_empty_set(self):
        self.assertTrue(check_subset((1, 2, 3), ()))

    def test_full_set(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    def test_subset_with_duplicates(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (1, 2)))

    def test_non_subset(self):
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_subset((1, 2, 3), "not a tuple")

        with self.assertRaises(TypeError):
            check_subset("not a tuple", (1, 2, 3))

        with self.assertRaises(TypeError):
            check_subset("not a tuple", "not a tuple")
