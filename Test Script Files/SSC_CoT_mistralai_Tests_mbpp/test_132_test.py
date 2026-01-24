import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_empty_input(self):
        self.assertEqual(tup_string(()), '')

    def test_single_input(self):
        self.assertEqual(tup_string(('x',)), 'x')

    def test_edge_cases(self):
        self.assertEqual(tup_string((1, 2, 3)), '123')
        self.assertEqual(tup_string((1, 2, 3, )), '123')
        self.assertEqual(tup_string((1, 2, 3, None)), '123')
        self.assertEqual(tup_string((1, 2, 3, 4, )), '1234')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tup_string(123)
        with self.assertRaises(TypeError):
            tup_string([1, 2, 3])
