import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))
        self.assertFalse(check_subset_list([1, 2, 3], [1, 2, 4]))

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))
        self.assertTrue(check_subset_list([], [1, 2, 3]))
        self.assertFalse(check_subset_list([1, 2, 3], []))

    def test_single_element_lists(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([1], [2]))

    def test_duplicates(self):
        self.assertTrue(check_subset_list([1, 2, 2], [1, 2]))
        self.assertFalse(check_subset_list([1, 2, 2], [1, 2, 2, 2]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_subset_list([1, 2, 3], [1, '2', 3])
        with self.assertRaises(TypeError):
            check_subset_list([1, 2, 3], 123)
        with self.assertRaises(TypeError):
            check_subset_list(123, [1, 2, 3])
