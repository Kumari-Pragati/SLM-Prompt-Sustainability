import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element([1, 1, 1], 1))
        self.assertFalse(check_element([1, 2, 3], 2))

    def test_empty_list(self):
        self.assertTrue(check_element([], 1))
        self.assertTrue(check_element([], None))

    def test_single_element_list(self):
        self.assertTrue(check_element([5], 5))
        self.assertFalse(check_element([5], 1))

    def test_mixed_types(self):
        self.assertFalse(check_element([1, 'a', True], 1))
        self.assertFalse(check_element([1, 'a', True], 'a'))
        self.assertFalse(check_element([1, 'a', True], True))

    def test_none_element(self):
        self.assertFalse(check_element([None, None, None], None))
        self.assertTrue(check_element([None], None))
