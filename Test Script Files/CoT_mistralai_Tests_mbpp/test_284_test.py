import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_check_element_with_matching_list(self):
        self.assertTrue(check_element([1, 1, 1], 1))

    def test_check_element_with_non_matching_list(self):
        self.assertFalse(check_element([1, 2, 3], 1))

    def test_check_element_with_empty_list(self):
        self.assertFalse(check_element([]))

    def test_check_element_with_single_element_list(self):
        self.assertFalse(check_element([1], 1))

    def test_check_element_with_none_type_input(self):
        self.assertRaises(TypeError, check_element, None, 1)

    def test_check_element_with_string_type_input(self):
        self.assertRaises(TypeError, check_element, ['a'], 'b')
