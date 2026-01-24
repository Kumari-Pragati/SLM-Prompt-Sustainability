import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c'), ('a', 'b')))

    def test_edge_case_empty_tuples(self):
        self.assertFalse(check_tuplex((), ()))

    def test_boundary_case_single_element_tuples(self):
        self.assertTrue(check_tuplex(('a',), ('a',)))
        self.assertFalse(check_tuplex(('a',), ('b',)))

    def test_complex_case_duplicates(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c', 'a'), ('a',)))

    def test_edge_case_large_tuples(self):
        large_tuple = tuple(range(1000))
        self.assertTrue(check_tuplex(large_tuple, large_tuple[:500]))

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            check_tuplex(None, ('a', 'b'))

    def test_invalid_input_non_tuple_first_argument(self):
        with self.assertRaises(TypeError):
            check_tuplex('not a tuple', ('a', 'b'))

    def test_invalid_input_non_tuple_second_argument(self):
        with self.assertRaises(TypeError):
            check_tuplex(('a', 'b'), 'not a tuple')
