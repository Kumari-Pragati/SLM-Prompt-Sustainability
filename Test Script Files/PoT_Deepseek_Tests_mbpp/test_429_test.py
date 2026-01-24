import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), (1 & 4, 2 & 5, 3 & 6))

    def test_empty_tuples(self):
        self.assertEqual(and_tuples((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(and_tuples((1), (4)), (1 & 4,))

    def test_unequal_length_tuples(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5)), (1 & 4, 2 & 5))

    def test_large_numbers(self):
        self.assertEqual(and_tuples((1000000000, 2000000000), (3000000000, 4000000000)),
                         (1000000000 & 3000000000, 2000000000 & 4000000000))

    def test_zero_elements(self):
        self.assertEqual(and_tuples((), (4, 5, 6)), ())

    def test_negative_elements(self):
        self.assertEqual(and_tuples((-1, 2, 3), (4, -5, 6)), (-1 & 4, 2 & -5, 3 & 6))
