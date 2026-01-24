import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_and_tuples(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), (0, 2, 6))
        self.assertEqual(and_tuples((1, 2, 3), (3, 2, 1)), (1, 2, 1))
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(and_tuples((1, 2, 3), ()), ())
        self.assertEqual(and_tuples((), (1, 2, 3)), ())
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6, 7)), (0, 2, 6))
