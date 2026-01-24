import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_repeat_tuples(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 2), ((1, 2, 3), (1, 2, 3)))
        self.assertEqual(repeat_tuples((1, 2, 3), 0), ())
        self.assertEqual(repeat_tuples((1, 2, 3), 1), ((1, 2, 3),))
        self.assertEqual(repeat_tuples((1, 2, 3), 3), ((1, 2, 3), (1, 2, 3), (1, 2, 3)))
        self.assertEqual(repeat_tuples((1, 2, 3), 4), ((1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3)))

    def test_repeat_tuples_empty(self):
        self.assertEqual(repeat_tuples((), 2), ((), ()))

    def test_repeat_tuples_single(self):
        self.assertEqual(repeat_tuples((1,), 2), ((1,), (1,)))
