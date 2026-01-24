import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertIsInstance(and_tuples((), ()), tuple)
        self.assertListEqual(and_tuples((), ()), ())

    def test_single_element_tuples(self):
        self.assertIsInstance(and_tuples((1,), (1,)), tuple)
        self.assertListEqual(and_tuples((1,), (1,)), (1,))
        self.assertIsInstance(and_tuples((1,), (2,)), tuple)
        self.assertListEqual(and_tuples((1,), (2,)), ())

    def test_multiple_element_tuples(self):
        self.assertIsInstance(and_tuples((1, 2, 3), (4, 5, 6)), tuple)
        self.assertListEqual(and_tuples((1, 2, 3), (4, 5, 6)), (1, 2))
        self.assertIsInstance(and_tuples((1, 2, 3), (3, 4, 5)), tuple)
        self.assertListEqual(and_tuples((1, 2, 3), (3, 4, 5)), (3,))
