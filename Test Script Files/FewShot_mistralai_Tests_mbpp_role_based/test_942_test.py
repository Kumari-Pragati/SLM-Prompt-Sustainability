import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_element_in_list(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))

    def test_element_not_in_list(self):
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_empty_list(self):
        self.assertFalse(check_element((1, 2, 3), []))

    def test_empty_tuple(self):
        self.assertFalse(check_element((), [1, 2, 3]))

    def test_list_with_none(self):
        self.assertFalse(check_element((1, 2, 3), [None, 1, 2, 3]))
