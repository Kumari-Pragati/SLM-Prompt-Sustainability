import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_all_elements_are_same(self):
        self.assertTrue(check_element([1, 1, 1], 1))

    def test_not_all_elements_are_same(self):
        self.assertFalse(check_element([1, 2, 3], 1))

    def test_empty_list(self):
        self.assertTrue(check_element([], 1))

    def test_list_with_different_elements(self):
        self.assertFalse(check_element([1, 2, 3], 2))
