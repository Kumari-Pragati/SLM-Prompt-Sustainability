import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(and_tuples((1, 2, 3, 4), (5, 2, 3, 6)), (2, 3))
        self.assertListEqual(and_tuples((10, 20, 30, 40), (5, 2, 3, 60)), ())
        self.assertListEqual(and_tuples((1, 1, 1, 1), (1, 0, 1, 1)), (1,))

    def test_edge_case(self):
        self.assertListEqual(and_tuples((1,), (2,)), ())
        self.assertListEqual(and_tuples((1, 2, 3), ()), ())
        self.assertListEqual(and_tuples((), (1, 2, 3)), ())

    def test_corner_case(self):
        self.assertListEqual(and_tuples((float('inf'),), (0,)), ())
        self.assertListEqual(and_tuples((0,), (float('inf'),)), ())
        self.assertListEqual(and_tuples((float('inf'), 0), (0, float('inf'))), ())
