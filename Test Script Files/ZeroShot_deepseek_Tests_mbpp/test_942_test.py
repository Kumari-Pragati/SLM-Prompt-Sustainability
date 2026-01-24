import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_positive_case(self):
        test_tup = ('a', 'b', 'c')
        check_list = ['a', 'd', 'e']
        self.assertTrue(check_element(test_tup, check_list))

    def test_negative_case(self):
        test_tup = ('a', 'b', 'c')
        check_list = ['d', 'e', 'f']
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_list(self):
        test_tup = ('a', 'b', 'c')
        check_list = []
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_tuple(self):
        test_tup = ()
        check_list = ['a', 'b', 'c']
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_both(self):
        test_tup = ()
        check_list = []
        self.assertFalse(check_element(test_tup, check_list))
