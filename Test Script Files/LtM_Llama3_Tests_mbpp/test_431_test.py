import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_common_element_true(self):
        self.assertTrue(common_element([1, 2, 3], [2, 3, 4]))

    def test_common_element_false(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))

    def test_common_element_empty_list1(self):
        self.assertFalse(common_element([], [1, 2, 3]))

    def test_common_element_empty_list2(self):
        self.assertFalse(common_element([1, 2, 3], []))

    def test_common_element_single_element(self):
        self.assertTrue(common_element([1], [1]))

    def test_common_element_multiple_common_elements(self):
        self.assertTrue(common_element([1, 2, 3], [2, 3, 4]))

    def test_common_element_no_common_elements(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))
