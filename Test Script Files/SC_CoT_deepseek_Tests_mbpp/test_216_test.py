import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))

    def test_subset_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))

    def test_non_subset_case(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5]))

    def test_same_elements_different_order(self):
        self.assertTrue(check_subset_list([1, 2, 3], [3, 1, 2]))

    def test_empty_list_in_second(self):
        self.assertTrue(check_subset_list([1, 2, 3], []))

    def test_single_element_lists(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([1], [2]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_subset_list("not a list", [1, 2, 3])
        with self.assertRaises(TypeError):
            check_subset_list([1, 2, 3], "not a list")
        with self.assertRaises(TypeError):
            check_subset_list("not a list", "not a list")
