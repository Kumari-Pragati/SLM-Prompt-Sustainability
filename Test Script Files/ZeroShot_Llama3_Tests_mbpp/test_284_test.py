import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_check_element_found(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 3))

    def test_check_element_not_found(self):
        self.assertFalse(check_element([1, 2, 3, 4, 5], 6))

    def test_check_element_found_first(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 1))

    def test_check_element_found_last(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 5))

    def test_check_element_found_middle(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 3))

    def test_check_element_empty_list(self):
        self.assertFalse(check_element([], 1))

    def test_check_element_single_element(self):
        self.assertTrue(check_element([1], 1))

    def test_check_element_multiple_elements(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 1) or check_element([1, 2, 3, 4, 5], 2) or check_element([1, 2, 3, 4, 5], 3) or check_element([1, 2, 3, 4, 5], 4) or check_element([1, 2, 3, 4, 5], 5))
