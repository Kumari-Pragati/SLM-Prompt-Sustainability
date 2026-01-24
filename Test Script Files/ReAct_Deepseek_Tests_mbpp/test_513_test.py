import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (('a', 'b'), ('c', 'd'))
        K = 'e'
        expected_output = [('a', 'b'), 'e', ('c', 'd'), 'e']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_empty_tuple(self):
        test_tup = ()
        K = 'e'
        expected_output = ['e']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_single_element_tuple(self):
        test_tup = (('a', 'b'),)
        K = 'e'
        expected_output = [('a', 'b'), 'e']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_duplicate_elements(self):
        test_tup = (('a', 'a'), ('b', 'b'))
        K = 'e'
        expected_output = [('a', 'a'), 'e', ('b', 'b'), 'e']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_large_tuple(self):
        test_tup = (('a', 'b'),) * 1000
        K = 'e'
        expected_output = [('a', 'b')] * 1000 + ['e']
        self.assertEqual(add_str(test_tup, K), expected_output)
