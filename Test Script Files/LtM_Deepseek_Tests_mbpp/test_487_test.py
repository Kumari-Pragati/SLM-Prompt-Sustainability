import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sort_tuple(((1, 2), (3, 4))), ((1, 2), (3, 4)))
        self.assertEqual(sort_tuple(((5, 6), (7, 8))), ((5, 6), (7, 8)))

    def test_edge_conditions(self):
        self.assertEqual(sort_tuple(()), ())
        self.assertEqual(sort_tuple(((1, 2),)), ((1, 2),))

    def test_boundary_conditions(self):
        self.assertEqual(sort_tuple(((1, 2), (2, 1))), ((1, 2), (2, 1)))
        self.assertEqual(sort_tuple(((2, 1), (1, 2))), ((1, 2), (2, 1)))

    def test_complex_cases(self):
        self.assertEqual(sort_tuple(((1, 2), (2, 1), (1, 1))), ((1, 1), (1, 2), (2, 1)))
        self.assertEqual(sort_tuple(((2, 1), (1, 2), (2, 2))), ((1, 2), (2, 1), (2, 2)))
