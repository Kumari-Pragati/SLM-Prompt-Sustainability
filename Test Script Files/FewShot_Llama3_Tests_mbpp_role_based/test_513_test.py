import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = ('a', 'b', 'c')
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_empty_tuple(self):
        test_tup = ()
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['d'])

    def test_single_element_tuple(self):
        test_tup = ('a',)
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, ['a', 'd'])

    def test_non_string_elements(self):
        test_tup = (1, 2, 3)
        K = 'd'
        result = add_str(test_tup, K)
        self.assertEqual(result, [1, 2, 3, 'd'])

    def test_non_tuple_input(self):
        test_tup = 'abc'
        K = 'd'
        with self.assertRaises(TypeError):
            add_str(test_tup, K)
