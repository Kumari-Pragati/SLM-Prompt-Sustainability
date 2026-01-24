import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_edge_conditions(self):
        self.assertEqual(and_tuples((), ()), ())
        self.assertEqual(and_tuples((1, 2, 3), (0, 0, 0)), (0, 0, 0))

    def test_boundary_conditions(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(and_tuples((0, 1, 2), (7, 8, 9)), (0, 1, 2))

    def test_complex_cases(self):
        self.assertEqual(and_tuples((1, 2, 3, 4), (5, 6, 7, 8)), (1, 2, 3, 4))
        self.assertEqual(and_tuples((1, 0, 1, 0), (0, 1, 0, 1)), (0, 0, 0, 0))
