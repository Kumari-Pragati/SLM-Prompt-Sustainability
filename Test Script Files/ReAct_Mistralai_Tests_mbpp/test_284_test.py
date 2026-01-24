import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_check_element_empty_list(self):
        self.assertFalse(check_element([], 1))

    def test_check_element_single_element_list(self):
        self.assertTrue(check_element([1], 1))

    def test_check_element_multiple_elements_list(self):
        self.assertTrue(check_element([1, 1, 1], 1))
        self.assertFalse(check_element([1, 1, 2], 1))

    def test_check_element_list_with_duplicates(self):
        self.assertTrue(check_element([1, 1, 1, 2, 2, 2], 2))

    def test_check_element_list_with_none(self):
        self.assertRaises(TypeError, check_element, [None], 1)

    def test_check_element_list_with_string(self):
        self.assertRaises(TypeError, check_element, ['a', 'a'], 'a')

    def test_check_element_list_with_mixed_types(self):
        self.assertRaises(TypeError, check_element, [1, 'a'], 1)
