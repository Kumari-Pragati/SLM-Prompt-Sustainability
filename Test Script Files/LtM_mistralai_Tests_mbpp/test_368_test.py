import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(repeat_tuples((1, 2), 3), ((1, 2), (1, 2), (1, 2)))
        self.assertEqual(repeat_tuples((3, 'a'), 2), ((3, 'a'), (3, 'a')))

    def test_edge_cases(self):
        self.assertEqual(repeat_tuples((0, 0), 1), ((0, 0),))
        self.assertEqual(repeat_tuples((1,), 0), ())
        self.assertEqual(repeat_tuples((1,), -1), ())

    def test_complex(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 4), ((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3)))
        self.assertEqual(repeat_tuples((1, 'a', 3.14), 2), ((1, 'a', 3.14), (1, 'a', 3.14)))
        self.assertEqual(repeat_tuples((True, False, 'x'), 0), ())
        self.assertEqual(repeat_tuples((None, 'a', 3), -1), ())
