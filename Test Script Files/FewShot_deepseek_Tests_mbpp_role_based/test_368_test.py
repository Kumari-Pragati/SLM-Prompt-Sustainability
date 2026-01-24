import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 3), [('a', 'b'), ('a', 'b'), ('a', 'b')])

    def test_edge_condition(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 0), [])

    def test_boundary_condition(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 1), [('a', 'b')])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            repeat_tuples('a', 'b')
