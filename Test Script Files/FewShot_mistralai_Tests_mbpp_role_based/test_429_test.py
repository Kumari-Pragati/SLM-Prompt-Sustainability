import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_and_tuples_same_length(self):
        self.assertEqual(and_tuples((1, 2, 3, 4), (5, 6, 7, 8)), (set(), set()))
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3, 4)), {1, 2})
        self.assertEqual(and_tuples((1, 2, 3), (1, 2)), {2})
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), set())

    def test_and_tuples_different_lengths(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2)), set())
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3, 4, 5)), set())
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3, 4)), {1, 2})
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3, 4, 5, 6)), set())
