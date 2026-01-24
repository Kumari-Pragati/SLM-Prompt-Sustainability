import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))

    def test_subset_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_not_subset_case(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5]))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset([1, 2, 2], [1, 2]))
        self.assertFalse(check_subset([1, 2, 2], [1, 2, 3]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_subset("1,2,3", [1, 2, 3])
        with self.assertRaises(TypeError):
            check_subset([1, 2, 3], "1,2,3")
        with self.assertRaises(TypeError):
            check_subset("1,2,3", "1,2,3")
