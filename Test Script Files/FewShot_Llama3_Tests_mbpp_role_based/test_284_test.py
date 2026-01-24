import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_found_element(self):
        list = [1, 2, 3, 4, 5]
        element = 4
        self.assertTrue(check_element(list, element))

    def test_not_found_element(self):
        list = [1, 2, 3, 4, 5]
        element = 6
        self.assertFalse(check_element(list, element))

    def test_empty_list(self):
        list = []
        element = 4
        self.assertFalse(check_element(list, element))

    def test_single_element_list(self):
        list = [4]
        element = 4
        self.assertTrue(check_element(list, element))

    def test_list_with_duplicates(self):
        list = [1, 2, 2, 3, 4, 4, 5]
        element = 4
        self.assertTrue(check_element(list, element))
