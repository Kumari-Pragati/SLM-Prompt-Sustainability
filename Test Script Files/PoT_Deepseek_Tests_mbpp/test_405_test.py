import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c'), ('a', 'b')))

    def test_edge_case_empty_tuples(self):
        self.assertFalse(check_tuplex((), ()))

    def test_boundary_case_single_element_tuples(self):
        self.assertTrue(check_tuplex(('a',), ('a',)))
        self.assertFalse(check_tuplex(('a',), ('b',)))

    def test_corner_case_repeated_elements(self):
        self.assertTrue(check_tuplex(('a', 'b', 'a'), ('a',)))

    def test_corner_case_nested_tuples(self):
        self.assertTrue(check_tuplex(('a', ('b', 'c')), ('a', ('b', 'c'))))
        self.assertFalse(check_tuplex(('a', ('b', 'c')), ('a', ('c', 'b'))))

    def test_corner_case_subsequence(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c'), ('a', 'b')))
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('b', 'c')))
