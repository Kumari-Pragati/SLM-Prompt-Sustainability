import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(and_tuples((1, 2, 3), (4, 2, 3)), (2, 3))
        self.assertListEqual(and_tuples((0, 1, 2), (3, 2, 1)), ())
        self.assertListEqual(and_tuples((5, 5, 5), (5, 5, 5)), (5, 5, 5))

    def test_edge_cases(self):
        self.assertListEqual(and_tuples((1,), (2,)), ())
        self.assertListEqual(and_tuples((1, 2), ()), ())
        self.assertListEqual(and_tuples((), (1, 2)), ())

    def test_complex(self):
        self.assertListEqual(and_tuples((1, 2, 3), (3, 4, 5)), (3,))
        self.assertListEqual(and_tuples((1, 2, 3), (3, 2, 1)), (3,))
        self.assertListEqual(and_tuples((float('inf'), 2, -1), (3, float('inf'), -2)), (3,))
