import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_add_str_with_valid_input(self):
        test_tup = ('a', 'b', 'c')
        K = 'd'
        expected_output = ['a', 'd', 'b', 'd', 'c', 'd']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_add_str_with_empty_input(self):
        test_tup = ()
        K = 'd'
        expected_output = []
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_add_str_with_single_element_input(self):
        test_tup = ('a',)
        K = 'd'
        expected_output = ['a', 'd']
        self.assertEqual(add_str(test_tup, K), expected_output)
