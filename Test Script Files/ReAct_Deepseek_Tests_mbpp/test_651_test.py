import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertTrue(check_subset((1, 2, 2, 3), (2, 2)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))

    def test_empty_tuples(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((1, 2, 3), ()))
        self.assertTrue(check_subset((), (1, 2, 3)))

    def test_single_element_tuples(self):
        self.assertTrue(check_subset((1,), (1,)))
        self.assertFalse(check_subset((1,), (2,)))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (2, 2)))
        self.assertFalse(check_subset((1, 2, 3), (2, 3, 4)))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            check_subset((1, 2, 3), "not a tuple")
        with self.assertRaises(TypeError):
            check_subset("not a tuple", (1, 2, 3))
        with self.assertRaises(TypeError):
            check_subset("not a tuple", "not a tuple")
