import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_and_tuples_typical(self):
        self.assertListEqual(and_tuples((1, 2, 3, 4), (5, 2, 3, 4, 5)), (2, 3, 4))
        self.assertListEqual(and_tuples((1, 0, 1, 0), (0, 1, 0, 1)), (0, 0, 0, 0))
        self.assertListEqual(and_tuples((10, 20, 30, 40), (5, 2, 3, 4)), (0, 0, 0, 0))

    def test_and_tuples_edge(self):
        self.assertListEqual(and_tuples((1,), (2,)), ())
        self.assertListEqual(and_tuples((1, 2, 3), ()), ())
        self.assertListEqual(and_tuples((), (1, 2, 3)), ())

    def test_and_tuples_invalid(self):
        self.assertRaises(TypeError, and_tuples, (1, 2, 3), 'not_a_tuple')
        self.assertRaises(TypeError, and_tuples, 'not_a_tuple', (1, 2, 3))
