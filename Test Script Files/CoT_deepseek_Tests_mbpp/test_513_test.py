import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3)
        K = 'test'
        expected_output = [(1, 'test'), (2, 'test'), (3, 'test')]
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_empty_tuple(self):
        test_tup = ()
        K = 'test'
        expected_output = []
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_single_element_tuple(self):
        test_tup = (1,)
        K = 'test'
        expected_output = [(1, 'test')]
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_string_elements(self):
        test_tup = ('a', 'b', 'c')
        K = 'test'
        expected_output = [('a', 'test'), ('b', 'test'), ('c', 'test')]
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_mixed_elements(self):
        test_tup = (1, 'a', 2, 'b', 3, 'c')
        K = 'test'
        expected_output = [(1, 'test'), ('a', 'test'), (2, 'test'), ('b', 'test'), (3, 'test'), ('c', 'test')]
        self.assertEqual(add_str(test_tup, K), expected_output)
