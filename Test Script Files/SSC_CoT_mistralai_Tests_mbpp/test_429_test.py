import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_normal(self):
        self.assertListEqual(and_tuples((1, 2, 3), (3, 4, 5)), (3,))
        self.assertListEqual(and_tuples((True, False, True), (False, True, False)), (False,))

    def test_edge_cases(self):
        self.assertListEqual(and_tuples((1,), (2,)), [])
        self.assertListEqual(and_tuples((1, 2, 3), ()), [])
        self.assertListEqual(and_tuples((), (1, 2, 3)), [])

    def test_boundary_cases(self):
        self.assertListEqual(and_tuples((0,), (0,)), [0])
        self.assertListEqual(and_tuples((-1,), (1,)), [])
        self.assertListEqual(and_tuples((1,), (-1,)), [])

    def test_special_cases(self):
        self.assertListEqual(and_tuples((0, 1, 0), (1, 0, 1)), (0,))
        self.assertListEqual(and_tuples((1, 2, 3), (3, 2, 1)), (3,))
