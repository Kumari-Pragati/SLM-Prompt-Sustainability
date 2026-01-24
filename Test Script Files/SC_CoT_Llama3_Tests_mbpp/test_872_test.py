import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_subset_true(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2, 3]))

    def test_subset_false(self):
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [6, 7, 8]))

    def test_subset_empty(self):
        self.assertTrue(check_subset([], []))

    def test_subset_single_element(self):
        self.assertTrue(check_subset([1], [1]))

    def test_subset_multiple_elements(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_subset_empty_list1(self):
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_subset_empty_list2(self):
        self.assertTrue(check_subset([1, 2, 3], []))

    def test_subset_list1_subset_list2(self):
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 4]))

    def test_subset_list1_superset_list2(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2, 3]))

    def test_subset_list1_subset_list2_subset(self):
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 4]))

    def test_subset_list1_superset_list2_superset(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5, 6], [1, 2, 3, 4]))

    def test_subset_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_subset('abc', [1, 2, 3])

    def test_subset_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            check_subset([1, 2, 3], 'abc')

    def test_subset_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            check_subset(None, [1, 2, 3])

    def test_subset_invalid_input_type4(self):
        with self.assertRaises(TypeError):
            check_subset([1, 2, 3], None)
