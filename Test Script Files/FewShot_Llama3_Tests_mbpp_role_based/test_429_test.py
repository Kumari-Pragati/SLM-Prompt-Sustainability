import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_and_tuples_empty(self):
        self.assertEqual(and_tuples((), (1, 2, 3)), ())

    def test_and_tuples_single_element(self):
        self.assertEqual(and_tuples((1,), (2,)), ((1 & 2),))

    def test_and_tuples_multiple_elements(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), ((1 & 4, 2 & 5, 3 & 6),))

    def test_and_tuples_mismatched_lengths(self):
        with self.assertRaises(IndexError):
            and_tuples((1, 2), (3, 4, 5, 6))

    def test_and_tuples_non_integer_elements(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 'a'), (2, 3))
