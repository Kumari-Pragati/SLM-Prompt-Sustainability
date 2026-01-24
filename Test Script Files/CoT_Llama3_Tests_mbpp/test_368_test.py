import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 2), ((1, 2, 3),) * 2)

    def test_edge_case_N_0(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 0), ())

    def test_edge_case_N_1(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 1), ((1, 2, 3),))

    def test_edge_case_N_negative(self):
        with self.assertRaises(TypeError):
            repeat_tuples((1, 2, 3), -1)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            repeat_tuples(123, 2)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            repeat_tuples((1, 2, 3), 'a')
