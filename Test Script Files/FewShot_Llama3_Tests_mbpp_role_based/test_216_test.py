import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):
    def test_subset_list(self):
        self.assertTrue(check_subset_list([[1, 2, 3], [1, 2, 3]], [[1, 2, 3]]))

    def test_subset_list_with_duplicates(self):
        self.assertTrue(check_subset_list([[1, 2, 3], [1, 2, 3]], [[1, 2, 3, 3]]))

    def test_subset_list_with_empty_list(self):
        self.assertTrue(check_subset_list([[], [1, 2, 3]], [[1, 2, 3]]))

    def test_subset_list_with_empty_sublist(self):
        self.assertTrue(check_subset_list([[1, 2, 3], []], [[1, 2, 3]]))

    def test_subset_list_with_non_list_input(self):
        with self.assertRaises(TypeError):
            check_subset_list([1, 2, 3], "not a list")

    def test_subset_list_with_non_list_input2(self):
        with self.assertRaises(TypeError):
            check_subset_list("not a list", [1, 2, 3])
