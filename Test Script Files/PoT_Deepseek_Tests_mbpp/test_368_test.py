import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 2), [('a', 'b'), ('a', 'b')])

    def test_edge_case_N_zero(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 0), [])

    def test_boundary_case_N_one(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 1), [('a', 'b')])

    def test_corner_case_empty_tuple(self):
        self.assertEqual(repeat_tuples((), 2), [(), ()])

    def test_exceptional_case_invalid_N(self):
        with self.assertRaises(TypeError):
            repeat_tuples(('a', 'b'), 'two')
