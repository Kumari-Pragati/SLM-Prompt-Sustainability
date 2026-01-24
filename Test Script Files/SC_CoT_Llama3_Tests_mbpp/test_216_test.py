import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))

    def test_subset(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))

    def test_superset(self):
        self.assertFalse(check_subset_list([1, 2, 3], [1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(check_subset_list([], []))

    def test_empty_subset(self):
        self.assertTrue(check_subset_list([1, 2, 3], []))

    def test_non_subset(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5]))

    def test_single_element_subset(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1]))

    def test_single_element_non_subset(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4]))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_subset_list('hello', [1, 2, 3])

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            check_subset_list([1, 2, 3], [1, 2, 3, 4, 5])
