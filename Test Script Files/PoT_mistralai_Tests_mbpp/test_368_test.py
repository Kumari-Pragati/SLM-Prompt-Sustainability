import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(repeat_tuples((1, 2), 3), ((1, 2), (1, 2), (1, 2)))

    def test_edge_case_single_tuple(self):
        self.assertEqual(repeat_tuples((3,), 5), ((3,), (3,), (3,), (3,), (3,)))

    def test_edge_case_zero_repetitions(self):
        self.assertEqual(repeat_tuples((4, 5), 0), ())

    def test_edge_case_negative_repetitions(self):
        self.assertRaises(ValueError, repeat_tuples, (6, 7), -1)

    def test_corner_case_empty_tuple(self):
        self.assertEqual(repeat_tuples((), 2), ())
