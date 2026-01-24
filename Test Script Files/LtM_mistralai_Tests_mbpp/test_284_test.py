import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_simple_match(self):
        self.assertTrue(check_element([1, 1, 1], 1))

    def test_list_empty(self):
        self.assertFalse(check_element([], 1))

    def test_single_element(self):
        self.assertTrue(check_element([1], 1))
        self.assertFalse(check_element([1], 2))

    def test_negative_numbers(self):
        self.assertTrue(check_element([-1, -1, -1], -1))
        self.assertFalse(check_element([-1, -1, 1], -1))

    def test_floats(self):
        self.assertTrue(check_element([3.14, 3.14, 3.14], 3.14))
        self.assertFalse(check_element([3.14, 3.14, 2.71], 3.14))

    def test_mixed_types(self):
        self.assertFalse(check_element([1, 'a', 1], 1))
