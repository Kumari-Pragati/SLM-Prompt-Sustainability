import unittest

from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element([1, 1, 1], 1))
        self.assertTrue(check_element(['a', 'a', 'a'], 'a'))
        self.assertTrue(check_element([True, True, True], True))

    def test_empty_list(self):
        self.assertTrue(check_element([], 'any_element'))

    def test_single_element_list(self):
        self.assertTrue(check_element(['single'], 'single'))
        self.assertFalse(check_element(['single'], 'different'))

    def test_mixed_types(self):
        self.assertFalse(check_element(['a', 1, True], 'a'))
        self.assertFalse(check_element(['a', 1, True], 1))
        self.assertFalse(check_element(['a', 1, True], True))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_element(123, 'any_element')
        with self.assertRaises(TypeError):
            check_element(['list', 'of', 'elements'], 123)
