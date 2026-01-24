import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_and_tuples_typical(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), (0, 1, 2))

    def test_and_tuples_empty(self):
        self.assertEqual(and_tuples((), (1, 2, 3)), ())

    def test_and_tuples_single(self):
        self.assertEqual(and_tuples((1, 2, 3), ()), ())

    def test_and_tuples_diff_lengths(self):
        self.assertEqual(and_tuples((1, 2, 3, 4), (5, 6)), (0, 1))

    def test_and_tuples_all_zeros(self):
        self.assertEqual(and_tuples((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_and_tuples_all_ones(self):
        self.assertEqual(and_tuples((1, 1, 1), (1, 1, 1)), (1, 1, 1))

    def test_and_tuples_mixed(self):
        self.assertEqual(and_tuples((1, 0, 1), (0, 1, 0)), (0, 0, 0))
