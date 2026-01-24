import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(left_rotate('abcde', 2), 'cdeab')
        self.assertEqual(left_rotate('12345', 1), '23451')

    def test_boundary_conditions(self):
        self.assertEqual(left_rotate('', 3), '')
        self.assertEqual(left_rotate('a', 0), 'a')
        self.assertEqual(left_rotate('abc', 3), 'abc')
        self.assertEqual(left_rotate('abc', 0), 'abc')

    def test_edge_cases(self):
        self.assertEqual(left_rotate('abcdef', 6), 'abcdef')
        self.assertEqual(left_rotate('abcdef', 7), 'defabc')
        self.assertEqual(left_rotate('abcdef', -1), 'fabcde')
