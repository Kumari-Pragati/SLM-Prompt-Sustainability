import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_typical_input(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertTrue(check_identical(list1, list2))

    def test_edge_case_empty_list(self):
        list1 = []
        list2 = []
        self.assertTrue(check_identical(list1, list2))

    def test_edge_case_single_element_list(self):
        list1 = [1]
        list2 = [1]
        self.assertTrue(check_identical(list1, list2))

    def test_edge_case_equal_length_lists(self):
        list1 = [1, 2, 3, 4]
        list2 = [1, 2, 3, 5]
        self.assertFalse(check_identical(list1, list2))

    def test_edge_case_non_equal_length_lists(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3, 4]
        self.assertFalse(check_identical(list1, list2))

    def test_edge_case_lists_with_duplicates(self):
        list1 = [1, 2, 2, 3]
        list2 = [1, 2, 2, 3]
        self.assertTrue(check_identical(list1, list2))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_identical(123, [1, 2, 3])

    def test_invalid_input_non_list2(self):
        with self.assertRaises(TypeError):
            check_identical([1, 2, 3], 123)
