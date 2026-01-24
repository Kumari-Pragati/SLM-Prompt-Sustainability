import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c'), ('a', 'b')))

    def test_edge_case_tuple_not_in_tuplex(self):
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('d', 'e')))

    def test_edge_case_empty_tuples(self):
        self.assertFalse(check_tuplex((), ()))
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ()))
        self.assertFalse(check_tuplex((), ('a', 'b')))

    def test_edge_case_single_element_tuples(self):
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('a',)))
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('b',)))
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('c',)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_tuplex(123, ('a', 'b'))
        with self.assertRaises(TypeError):
            check_tuplex(('a', 'b', 'c'), 123)
        with self.assertRaises(TypeError):
            check_tuplex(123, 123)
