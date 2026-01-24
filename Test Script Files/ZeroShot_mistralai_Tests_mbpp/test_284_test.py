import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_element([], 1))

    def test_single_element_list(self):
        self.assertTrue(check_element([1], 1))
        self.assertFalse(check_element([1], 2))

    def test_multiple_elements_list(self):
        self.assertTrue(check_element([1, 1], 1))
        self.assertFalse(check_element([1, 1], 2))

    def test_list_with_different_elements(self):
        self.assertFalse(check_element([1, 2], 1))
        self.assertFalse(check_element([1, 2], 2))
