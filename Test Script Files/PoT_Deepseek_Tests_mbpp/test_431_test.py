import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(common_element([1, 2, 3], [3, 4, 5]))

    def test_typical_case_2(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))

    def test_one_empty_list(self):
        self.assertFalse(common_element([], [1, 2, 3]))

    def test_same_elements(self):
        self.assertTrue(common_element([1, 2, 3], [1, 2, 3]))

    def test_duplicate_elements(self):
        self.assertTrue(common_element([1, 2, 2], [2, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(common_element([-1, -2, -3], [-3, -4, -5]))

    def test_large_numbers(self):
        self.assertTrue(common_element([1000000, 2000000, 3000000], [3000000, 4000000, 5000000]))
