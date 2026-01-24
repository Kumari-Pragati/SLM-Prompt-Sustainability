import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_common_element_in_both_lists(self):
        self.assertTrue(common_element([1, 2, 3], [2, 4, 5]))

    def test_common_element_in_first_list(self):
        self.assertTrue(common_element([1, 2, 2], [3, 4, 5]))

    def test_common_element_in_second_list(self):
        self.assertTrue(common_element([1, 2, 3], [1, 2, 3]))

    def test_no_common_element(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))

    def test_empty_list1(self):
        self.assertFalse(common_element([], [1, 2, 3]))

    def test_empty_list2(self):
        self.assertFalse(common_element([1, 2, 3], []))

    def test_single_element_list1(self):
        self.assertTrue(common_element([1], [1, 2, 3]))

    def test_single_element_list2(self):
        self.assertTrue(common_element([1, 2, 3], [1]))
