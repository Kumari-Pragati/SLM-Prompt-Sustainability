import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(left_rotate('abcde', 2), 'cdeab')
        self.assertEqual(left_rotate('12345', 3), '45123')

    def test_edge_cases(self):
        self.assertEqual(left_rotate('', 2), '')
        self.assertEqual(left_rotate('a', 0), 'a')
        self.assertEqual(left_rotate('abc', 0), 'abc')
        self.assertEqual(left_rotate('abc', 3), 'abc')
        self.assertEqual(left_rotate('abc', 4), 'abc')

    def test_boundary_conditions(self):
        self.assertEqual(left_rotate('abcde', 5), 'abcde')
        self.assertEqual(left_rotate('abcde', 6), 'abcde')
