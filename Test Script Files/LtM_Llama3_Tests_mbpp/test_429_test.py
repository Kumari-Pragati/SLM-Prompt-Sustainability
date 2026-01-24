import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_simple_and(self):
        self.assertEqual(and_tuples((1, 2), (3, 4)), (0, 0))

    def test_empty_input(self):
        self.assertEqual(and_tuples((), (1, 2)), ())

    def test_single_tuple(self):
        self.assertEqual(and_tuples((1, 2), ()), ())

    def test_tuple_of_tuples(self):
        self.assertEqual(and_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), ((0, 0), (0, 0)))

    def test_and_with_max_value(self):
        self.assertEqual(and_tuples((255, 255), (255, 255)), (255, 255))

    def test_and_with_min_value(self):
        self.assertEqual(and_tuples((0, 0), (0, 0)), (0, 0))

    def test_and_with_max_and_min_values(self):
        self.assertEqual(and_tuples((255, 0), (255, 0)), (0, 0))
