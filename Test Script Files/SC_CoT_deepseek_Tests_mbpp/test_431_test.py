import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(common_element([1, 2, 3], [3, 4, 5]))

    def test_no_common_element(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))

    def test_single_element_lists(self):
        self.assertFalse(common_element([1], [2]))
        self.assertTrue(common_element([1], [1]))

    def test_duplicate_elements(self):
        self.assertTrue(common_element([1, 2, 2], [2, 3, 4]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            common_element([1, 2, 3], 'not a list')
        with self.assertRaises(TypeError):
            common_element('not a list', [1, 2, 3])
        with self.assertRaises(TypeError):
            common_element('not a list', 'not a list')
