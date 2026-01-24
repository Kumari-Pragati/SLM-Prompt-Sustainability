import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(common_element([1, 2, 3], [2, 3, 4]))

    def test_no_common_element(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))

    def test_one_empty_list(self):
        self.assertFalse(common_element([1, 2, 3], []))

    def test_same_elements(self):
        self.assertTrue(common_element([1, 1, 1], [1, 1, 1]))

    def test_negative_numbers(self):
        self.assertTrue(common_element([-1, 0, 1], [0, 1, -1]))

    def test_mixed_types(self):
        self.assertTrue(common_element([1, 'a', True], ['a', 1, True]))
