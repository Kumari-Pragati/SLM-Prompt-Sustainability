import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 2), [('a', 'b'), ('a', 'b')])

    def test_empty_tuple(self):
        self.assertEqual(repeat_tuples((), 3), [(), (), ()])

    def test_negative_N(self):
        self.assertEqual(repeat_tuples(('x', 'y'), -1), [])

    def test_zero_N(self):
        self.assertEqual(repeat_tuples(('p', 'q'), 0), [])

    def test_large_N(self):
        self.assertEqual(len(repeat_tuples(('m', 'n'), 1000)), 1000)
