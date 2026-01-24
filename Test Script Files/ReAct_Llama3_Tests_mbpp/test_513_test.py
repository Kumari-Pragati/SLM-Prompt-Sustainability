import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical_case(self):
        test_tup = ('a', 'b', 'c')
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['d'])

    def test_edge_case_single_element_tuple(self):
        test_tup = ('a',)
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['a', 'd'])

    def test_edge_case_single_element_str(self):
        test_tup = 'a'
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['a', 'd'])

    def test_edge_case_empty_str(self):
        test_tup = ''
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['d'])

    def test_error_case_non_tuple_input(self):
        test_tup = 'a'
        K = 'd'
        with self.assertRaises(TypeError):
            add_str(test_tup, K)

    def test_error_case_non_str_input(self):
        test_tup = (1, 2, 3)
        K = 'd'
        with self.assertRaises(TypeError):
            add_str(test_tup, K)
