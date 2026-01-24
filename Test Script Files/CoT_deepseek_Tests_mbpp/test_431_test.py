import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4]
        list2 = [3, 4, 5, 6]
        self.assertTrue(common_element(list1, list2))

    def test_no_common_element(self):
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        self.assertFalse(common_element(list1, list2))

    def test_empty_lists(self):
        list1 = []
        list2 = []
        self.assertFalse(common_element(list1, list2))

    def test_one_empty_list(self):
        list1 = []
        list2 = [1, 2, 3, 4]
        self.assertFalse(common_element(list1, list2))

    def test_identical_lists(self):
        list1 = [1, 2, 3, 4]
        list2 = [1, 2, 3, 4]
        self.assertTrue(common_element(list1, list2))

    def test_duplicate_elements(self):
        list1 = [1, 2, 2, 3, 4]
        list2 = [2, 3, 4, 5, 6]
        self.assertTrue(common_element(list1, list2))

    def test_negative_numbers(self):
        list1 = [-1, -2, -3, -4]
        list2 = [-3, -4, -5, -6]
        self.assertTrue(common_element(list1, list2))

    def test_large_numbers(self):
        list1 = [1000000, 2000000, 3000000, 4000000]
        list2 = [3000000, 4000000, 5000000, 6000000]
        self.assertTrue(common_element(list1, list2))
