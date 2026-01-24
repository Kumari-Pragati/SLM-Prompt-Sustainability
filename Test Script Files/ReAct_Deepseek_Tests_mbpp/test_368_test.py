import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3)
        N = 3
        expected_result = ((1, 2, 3),) * N
        self.assertEqual(repeat_tuples(test_tup, N), expected_result)

    def test_edge_case_N_zero(self):
        test_tup = (1, 2, 3)
        N = 0
        expected_result = ()
        self.assertEqual(repeat_tuples(test_tup, N), expected_result)

    def test_edge_case_N_one(self):
        test_tup = (1, 2, 3)
        N = 1
        expected_result = ((1, 2, 3),)
        self.assertEqual(repeat_tuples(test_tup, N), expected_result)

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        N = 3
        expected_result = ()
        self.assertEqual(repeat_tuples(test_tup, N), expected_result)

    def test_error_case_negative_N(self):
        test_tup = (1, 2, 3)
        N = -1
        with self.assertRaises(ValueError):
            repeat_tuples(test_tup, N)
