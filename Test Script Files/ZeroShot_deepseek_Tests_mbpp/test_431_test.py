import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_common_element_exists(self):
        self.assertTrue(common_element([1, 2, 3], [2, 3, 4]))

    def test_common_element_not_exists(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))

    def test_single_element_lists(self):
        self.assertFalse(common_element([1], [2]))
        self.assertTrue(common_element([1], [1]))

    def test_duplicate_elements(self):
        self.assertTrue(common_element([1, 2, 2], [2, 3, 4]))
