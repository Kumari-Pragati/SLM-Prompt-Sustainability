import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(difference(1), 1)
        self.assertEqual(difference(2), 9)
        self.assertEqual(difference(3), 35)
        self.assertEqual(difference(4), 84)
        self.assertEqual(difference(5), 165)

    def test_zero(self):
        self.assertEqual(difference(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(difference(-1), 1)
        self.assertEqual(difference(-2), 9)
        self.assertEqual(difference(-3), 35)
        self.assertEqual(difference(-4), 84)
        self.assertEqual(difference(-5), 165)
