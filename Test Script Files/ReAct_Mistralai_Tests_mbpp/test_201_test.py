import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_single_element(self):
        self.assertTrue(chkList([1]))

    def test_empty_list(self):
        self.assertFalse(chkList([]))

    def test_multiple_elements(self):
        self.assertFalse(chkList([1, 2]))

    def test_duplicate_elements(self):
        self.assertTrue(chkList([1, 1]))

    def test_single_element_type_error(self):
        with self.assertRaises(TypeError):
            chkList([1, 'a'])

    def test_empty_list_type_error(self):
        with self.assertRaises(TypeError):
            chkList(1)
