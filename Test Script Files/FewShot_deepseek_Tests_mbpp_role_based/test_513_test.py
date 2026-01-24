import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = ('a', 'b', 'c')
        K = 'd'
        expected_output = ['a', 'd', 'b', 'd', 'c', 'd']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_edge_condition(self):
        test_tup = ()
        K = 'd'
        expected_output = []
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_boundary_condition(self):
        test_tup = ('a',)
        K = 'd'
        expected_output = ['a', 'd']
        self.assertEqual(add_str(test_tup, K), expected_output)

    def test_invalid_input(self):
        test_tup = 123
        K = 'd'
        with self.assertRaises(TypeError):
            add_str(test_tup, K)
