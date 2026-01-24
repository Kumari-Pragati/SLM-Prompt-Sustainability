import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_simple_sort(self):
        self.assertEqual(sort_tuple((1, 'a')), [(1, 'a')])
        self.assertEqual(sort_tuple((3, 'b')), [(3, 'b')])
        self.assertEqual(sort_tuple((2, 'a'), (1, 'b')), [(1, 'a'), (2, 'b')])

    def test_edge_cases(self):
        self.assertEqual(sort_tuple((-1, 'z')), [(-1, 'z')])
        self.assertEqual(sort_tuple((), ()), ())
        self.assertEqual(sort_tuple((0, 'a'), (0, 'b')), [(0, 'a'), (0, 'b')])

    def test_complex_sort(self):
        self.assertEqual(sort_tuple((3, 'z'), (1, 'y'), (2, 'x')), [(1, 'y'), (2, 'x'), (3, 'z')])
        self.assertEqual(sort_tuple((3, 'z'), (1, 'y'), (2, 'x'), (0, 'w')), [(0, 'w'), (1, 'y'), (2, 'x'), (3, 'z')])
        self.assertEqual(sort_tuple((3, 'z'), (1, 'y'), (2, 'x'), (0, 'w'), (4, 'v')), [(0, 'w'), (1, 'y'), (2, 'x'), (3, 'z'), (4, 'v')])
