import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), 3)
        self.assertEqual(len_log([['x', 'y', 'z'], ['w', 'v', 'u'], ['t', 's', 'r']]), 3)

    def test_edge_cases(self):
        self.assertEqual(len_log([['a']]), 1)
        self.assertEqual(len_log([['a', 'b'], ['c']]), 2)
        self.assertEqual(len_log([['a', 'b', 'c'], ['d'], ['e', 'f', 'g']]), 3)

    def test_boundary_cases(self):
        self.assertEqual(len_log([['a'] * 1000]], 1)
        self.assertEqual(len_log([['a'] * 10000]], 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            len_log(123)
        with self.assertRaises(TypeError):
            len_log('abc')
