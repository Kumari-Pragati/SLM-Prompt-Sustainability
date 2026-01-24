import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_min_of_two_positive_numbers(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(2, 1), 1)
        self.assertEqual(min_of_two(1, 1), 1)

    def test_min_of_two_negative_numbers(self):
        self.assertEqual(min_of_two(-1, -2), -1)
        self.assertEqual(min_of_two(-2, -1), -1)
        self.assertEqual(min_of_two(-1, -1), -1)

    def test_min_of_two_zero(self):
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(1, 0), 0)
        self.assertEqual(min_of_two(0, 0), 0)
