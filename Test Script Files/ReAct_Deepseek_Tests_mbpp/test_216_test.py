import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list([], []))

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))

    def test_single_element_lists(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([2], [1]))

    def test_multiple_elements_lists(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertFalse(check_subset_list([1, 2, 3], [1, 3]))
        self.assertFalse(check_subset_list([1, 2, 3], [2, 3]))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset_list([1, 1, 2], [1, 2]))
        self.assertFalse(check_subset_list([1, 2, 2], [1, 2, 2]))

    def test_non_integer_elements(self):
        self.assertTrue(check_subset_list(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertFalse(check_subset_list(['a', 'b', 'c'], ['a', 'c']))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            check_subset_list([1, 2, 3], 'not a list')
        with self.assertRaises(TypeError):
            check_subset_list('not a list', [1, 2, 3])
        with self.assertRaises(TypeError):
            check_subset_list('not a list', 'not a list')
