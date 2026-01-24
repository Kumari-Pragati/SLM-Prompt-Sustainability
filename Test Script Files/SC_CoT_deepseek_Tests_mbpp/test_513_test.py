import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (('a', 'b'), ('c', 'd'))
        K = 'e'
        expected_output = [('a', 'e'), ('b', 'e'), ('c', 'e'), ('d', 'e')]
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_empty_tuple(self):
        test_tup = ()
        K = 'e'
        expected_output = []
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_single_element_tuple(self):
        test_tup = (('a', 'b'),)
        K = 'e'
        expected_output = [('a', 'e'), ('b', 'e')]
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_large_tuple(self):
        test_tup = (('a', 'b'),) * 1000
        K = 'e'
        expected_output = [(ele, 'e') for ele in ('a', 'b')] * 1000
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_invalid_input(self):
        test_tup = (('a', 'b'), 'c')
        K = 'e'
        with self.assertRaises(TypeError):
            add_str(test_tup, K)
