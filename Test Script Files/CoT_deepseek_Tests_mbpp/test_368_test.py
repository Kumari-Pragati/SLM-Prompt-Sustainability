import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 3), [('a', 'b'), ('a', 'b'), ('a', 'b')])

    def test_single_element_tuple(self):
        self.assertEqual(repeat_tuples(('a',), 2), [('a',), ('a',)])

    def test_empty_tuple(self):
        self.assertEqual(repeat_tuples((), 3), [(), (), ()])

    def test_N_equals_zero(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 0), [])

    def test_invalid_N(self):
        with self.assertRaises(TypeError):
            repeat_tuples(('a', 'b'), '3')

    def test_invalid_tuple(self):
        with self.assertRaises(TypeError):
            repeat_tuples('a', 2)
