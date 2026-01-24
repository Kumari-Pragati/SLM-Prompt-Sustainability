import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 3), ((1, 2, 3), ) * 3)

    def test_edge_case_N_zero(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 0), ())

    def test_edge_case_N_one(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 1), ((1, 2, 3), ))

    def test_edge_case_N_negative(self):
        with self.assertRaises(TypeError):
            repeat_tuples((1, 2, 3), -1)

    def test_edge_case_N_non_integer(self):
        with self.assertRaises(TypeError):
            repeat_tuples((1, 2, 3), 3.5)

    def test_edge_case_test_tup_empty(self):
        self.assertEqual(repeat_tuples((), 3), (()) * 3)

    def test_edge_case_test_tup_single_element(self):
        self.assertEqual(repeat_tuples((4,), 3), ((4, ), ) * 3)
