import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_min_of_two_positive_numbers(self):
        self.assertEqual(min_of_two(3, 2), 2)

    def test_min_of_two_negative_numbers(self):
        self.assertEqual(min_of_two(-3, -2), -3)

    def test_min_of_two_mixed_numbers(self):
        self.assertEqual(min_of_two(-3, 2), -3)

    def test_min_of_two_equal_numbers(self):
        self.assertEqual(min_of_two(3, 3), 3)
