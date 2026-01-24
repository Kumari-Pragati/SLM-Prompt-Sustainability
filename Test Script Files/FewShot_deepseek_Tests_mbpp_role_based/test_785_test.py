import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3))

    def test_edge_condition(self):
        self.assertEqual(tuple_str_int(''), ())

    def test_boundary_condition(self):
        self.assertEqual(tuple_str_int('0'), (0,))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_str_int('a, b, c')
