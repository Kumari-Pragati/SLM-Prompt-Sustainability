import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3)
        N = 3
        result = repeat_tuples(test_tup, N)
        self.assertEqual(result, ((1, 2, 3), ) * 3)

    def test_edge_case_N_zero(self):
        test_tup = (4, 5, 6)
        N = 0
        result = repeat_tuples(test_tup, N)
        self.assertEqual(result, ())

    def test_edge_case_N_one(self):
        test_tup = (7, 8, 9)
        N = 1
        result = repeat_tuples(test_tup, N)
        self.assertEqual(result, ((7, 8, 9), ))

    def test_edge_case_N_negative(self):
        test_tup = (10, 11, 12)
        N = -1
        with self.assertRaises(TypeError):
            repeat_tuples(test_tup, N)

    def test_invalid_input_type(self):
        test_tup = "invalid"
        N = 2
        with self.assertRaises(TypeError):
            repeat_tuples(test_tup, N)
