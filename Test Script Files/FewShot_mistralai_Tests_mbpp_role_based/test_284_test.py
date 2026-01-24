import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_element_in_list(self):
        self.assertTrue(check_element([1, 2, 3], 2))

    def test_element_not_in_list(self):
        self.assertFalse(check_element([1, 2, 3], 4))

    def test_empty_list(self):
        self.assertFalse(check_element([]))

    def test_single_element_list(self):
        self.assertTrue(check_element([1]))

    def test_list_with_duplicates(self):
        self.assertTrue(check_element([1, 1, 2, 3], 1))
