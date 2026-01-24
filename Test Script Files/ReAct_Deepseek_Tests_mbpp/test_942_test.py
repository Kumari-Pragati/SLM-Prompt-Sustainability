import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        test_tup = ('a', 'b', 'c')
        check_list = ['b', 'c', 'd']
        self.assertTrue(check_element(test_tup, check_list))

    def test_typical_case_no_match(self):
        test_tup = ('a', 'b', 'c')
        check_list = ['e', 'f', 'g']
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_tup(self):
        test_tup = ()
        check_list = ['a', 'b', 'c']
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_check_list(self):
        test_tup = ('a', 'b', 'c')
        check_list = []
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_both(self):
        test_tup = ()
        check_list = []
        self.assertFalse(check_element(test_tup, check_list))

    def test_single_element_in_tup(self):
        test_tup = ('a',)
        check_list = ['a', 'b', 'c']
        self.assertTrue(check_element(test_tup, check_list))

    def test_single_element_not_in_tup(self):
        test_tup = ('a',)
        check_list = ['b', 'c', 'd']
        self.assertFalse(check_element(test_tup, check_list))
