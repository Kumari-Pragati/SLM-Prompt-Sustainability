import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(difference(5), 110)

    def test_smallest_possible_input(self):
        self.assertEqual(difference(1), 1)

    def test_largest_possible_input(self):
        self.assertEqual(difference(100), 5005000)

    def test_zero_input(self):
        self.assertEqual(difference(0), 0)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            difference(-5)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            difference(5.5)
