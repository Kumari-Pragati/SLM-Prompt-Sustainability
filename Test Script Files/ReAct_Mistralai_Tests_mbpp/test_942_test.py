import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_element((), []))

    def test_single_element(self):
        self.assertTrue(check_element((1,), [1]))
        self.assertFalse(check_element((1,), [2]))

    def test_multiple_elements(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_duplicate_elements(self):
        self.assertTrue(check_element((1, 1, 2, 3), [1, 2, 3]))

    def test_empty_tuple(self):
        self.assertFalse(check_element((), [1, 2, 3]))

    def test_single_element_tuple(self):
        self.assertTrue(check_element((1,), []))
        self.assertFalse(check_element((1,), [1]))

    def test_list_with_none(self):
        self.assertTrue(check_element((1,), [None]))

    def test_list_with_multiple_none(self):
        self.assertTrue(check_element((1,), [None, None, 1]))
